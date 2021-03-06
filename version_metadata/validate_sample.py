from .sraparse import SRAParseObjSet, SRAParseObj,  XMLValidator
from .utils import cmn, json2, logger
from .validate_json import JsonSchema
from .ihec_validator_base import  IHECJsonValidator
from . import validate_main
from . import utils
from . import sample_semantic_rules

class SampleValidator(IHECJsonValidator):
	def normalize_tags(self, hashed):
		fix_tag_names =  { self.normalize(k) :v for k, v in hashed.items()}	
		if 'donor_age' in fix_tag_names:
			try:
				fix_tag_names['donor_age'] = [int(val) for val in fix_tag_names['donor_age']]
			except Exception as err:
				logger.warn( '#__warning: failed to cast donor age to number\n'.format(err) + str(fix_tag_names))
		return fix_tag_names 

	def __init__(self, sra, validators, ignore_rules=None):
		super(SampleValidator, self).__init__(validators)
		if ignore_rules is None: ignore_rules = []
		self.semantic_rules = [e for e in dir(sample_semantic_rules) if e.startswith('rule_') and not e in ignore_rules]
		self.normalize = lambda t: t.lower().replace(' ', '_')
		self.sra = sra
		self.xmljson = self.sra.obj_xmljson()
		for (xml, attrs) in self.xmljson:
			logger(u'\n#__normalizingTags:{0}\n'.format(attrs['title']))
			attrs['attributes'] = self.normalize_tags(attrs['attributes'])
		logger("\n\n")
		


	def validate_semantics(self, attrs):
		attributes = attrs['attributes']
		failed = list()
		status = True
		if 'donor_age_unit' in attributes and attributes['donor_age_unit'] == 'year' and isinstance(attributes['donor_age'], int):
			age = int(attributes['donor_age'])
			if age > 90:
				logger('#__error: Donors over 90 years of age should be entered as "90+"\n')
				status = False 
				failed.append('semantic_rule:'+'\'Donors over 90 years of age should be entered as "90+"\'=failed')
		try:
		#if True:
			for rule_name in self.semantic_rules:
				f = getattr(sample_semantic_rules, rule_name)
				try:
					semantic_err = ""
					ok = f(attributes)
				except Exception as err:
					semantic_err = " , " + str(err)
					ok = False
				status = status and ok
				if not ok:
					print('__semantic_validation_failure__', rule_name + '=failed' + semantic_err)
					#failed.append(rule_name)
					failed.append('semantic_rule:' + rule_name + '=failed' + semantic_err )
			return status, failed
		except KeyError as e:
		#else:
			logger.warn('#warn keyerror in validate_semantics, probably is not even syntactically valid:{0}\n'.format(e))
			return False, failed







		return True



def main(args):
	print (args['-config'])
	outfile = args['-out']
	config = json2.loadf(args['-config'])
	xml_validator = XMLValidator(config["sra"]["sample"])
	ihec_validators = cmn.safedict([(schema["version"] ,  JsonSchema(schema["schema"], args, version=schema["version"])) for schema in config["ihec"]["sample"]])
	
	objtype = 'SAMPLE'
	objset = 'SAMPLE_SET'

	validated = list()
	xmllist = args.args()
	nObjs = 0
	sample_validator = dict()
	for e in xmllist:
		sra = SRAParseObjSet.from_file(e)
		nObjs += sra.nOffspring()
		if not sra.xml.getroot().tag  == objset:
			utils.sanity_check_fail('__unexpected_xmltype:' + e)
		if not sra.is_valid__xml(xml_validator) or args.has("-not-sra-xml-but-try"):
			utils.sanity_check_fail('__invalid_xml:' + e)
		v = SampleValidator(sra, ihec_validators)
		validated.extend(v.is_valid_ihec())
		sample_validator[e] = v 

	versioned_xml = ['<{0}>'.format(objset) ]
	for e in validated:
		(version, xml, tag) = e
		sra_versioned = SRAParseObj(xml)
		sra_versioned.add_attribute("VALIDATED_AGAINST_METADATA_SPEC", "{0}/{1}".format(version, objtype))
		versioned_xml.append(sra_versioned.tostring())
	versioned_xml.append('</{0}>'.format(objset))


	return validate_main.main(args, versioned_xml, validated, nObjs, sample_validator, xml_validator)




	





