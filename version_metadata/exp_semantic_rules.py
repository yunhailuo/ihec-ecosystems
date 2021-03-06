import re
from . import validate_ontology

verbose = True


class UMIValidator:
	def __init__(self):
		self.umi_regex= re.compile('((\d+)(T|B|M|S))+')
	def __call__(self, term):
		# http://fulcrumgenomics.github.io/fgbio/tools/latest/ExtractUmisFromBam.html
		term = term.strip()
		if len(term) == 0: return False
		
		if not term[-1] in 'TBMS': return False
		
		term2 = term.split('+')[0]
		if not len(term2) in [len(term)-2, len(term)]: return False
		
		matched = self.umi_regex.match(term2)
		if not matched: return False
		(start, end) = matched.span()
		return end == len(term2) and start == 0
	def tests():
		umi = UMIValidator()
		good = '3M2S75T'
		good2 =  '3M2S+T'
		assert umi(good)
		assert umi(good2)
		assert not umi("")
		assert not umi("A"+ good)
		assert not umi(good + "A")
		assert not umi("3M2S++T")
		return True

umi_validator = UMIValidator()

def rule_miRNA_smRNA_strategy(attributes):
	""" {
		"applies" : ["rna-seq", "experiment_type"],
		"description" : "If 'experiment_type' is 'smRNA-Seq', then 'library_strategy' must be set to 'miRNA-Seq'"
		
	}  """

	if verbose:
		print('#__rule:', rule_miRNA_smRNA_strategy.__name__,)

	if not 'experiment_type' in attributes:
		return True
	try:
		miRNA_experiment_type =  attributes['experiment_type'][0] in ['smRNA-Seq']	
		miRNA_strategy = attributes['library_strategy'][0] in ['miRNA-Seq']
		validation_status = miRNA_strategy  if miRNA_experiment_type else not miRNA_strategy
		return validation_status
	except Exception as e:
		return False

def rule_chip_umi_read_structure(attributes):
	""" {
		"applies" : ["chip-seq", "experiment_type"],
		"description" : "If 'umi_enabled' is 'true', then 'umi_read_structure' must be valid"
	} """
	def read_struct_valid(struct):
		if struct is None: return False
		if not struct.strip(): return False
		else:
			return umi_validator(struct)

	if not 'experiment_type' in attributes and not "experiment_target_histone" in attributes and not "experiment_target_tf" in attributes:
		return True
		
	if not attributes['experiment_type'][0] in ['ChIP-Seq']:
		if verbose: print('#__rule:', rule_chip_umi_read_structure.__name__, '__does_not_apply__') 
		return True
	elif verbose:
		print('#__rule:', rule_chip_umi_read_structure.__name__) 

	is_umi = attributes.get('umi_enabled')[0]
	if not is_umi in ['true', 'false']:
		return False
	elif is_umi in  ["true"]:
		return read_struct(attributes.get("umi_read_structure", [None])[0])
	else:
		return True


def rule_valid_experiment_ontology_curie(attr):
	""" {
        "applies" : ["*", "experiment_ontology_curie"],
        "description" : "'experiment_ontology_curie' attributes must validate"
	} """
	if not "experiment_ontology_curie" in attr: return True
	else:
		return validate_ontology.check_term(attr["experiment_ontology_curie"], "experiment_ontology_curie")


def rule_valid_molecule_ontology_curie(attr):
	""" {
        "applies" : ["*", "molecule_ontology_curie"],
        "description" : "'molecule_ontology_curie' attributes must validate"
	} """
	if not "molecule_ontology_curie" in attr: return True
	else:
		return validate_ontology.check_term(attr["molecule_ontology_curie"], "molecule_ontology_curie")

def rule_valid_histone_target(attr):
	""" {
        "applies" : ["ChIP-Seq", "experiment_target_histone"],
        "description" : "'experiment_target_histone' attributes must be 'NA' only for ChIP-Seq Input"
    } """
	histone = attr.get('experiment_target_histone', [''])[0]
	if attr.get('experiment_type', [""])[0].lower() in ['ChIP-Seq Input'.lower()]:
		return histone == 'NA'
	else:
		return histone != 'NA'

if __name__ == "__main__":
	print("__umi_tests_ok__", UMIValidator.tests())
