#!/usr/bin/python
# -*- coding: utf-8 -*-
# Code by Javik
# Update by @FreeManRepo

import re
import uuid

from plugin import *

from siriObjects.baseObjects import *
from siriObjects.uiObjects import *
from siriObjects.systemObjects import *
from siriObjects.contactObjects import *

class meCard(Plugin):
	
	@register("en-US", "(Who am I.*)|(What's my name.*)")
	@register("es-MX", "(Cual es mi nombre.*)|(Como me llamo.*)|(Quien soy.*)")
	
	def mePerson(self, speech, language):
		if language == 'en-US':
			self.say("You're {0}, that's what you told me. anyway.".format(self.user_name()))		
		elif language == 'es-MX':
			self.say("Tu eres {0}, eso es lo que me dijiste.".format(self.user_name()))	
			
		person_search = PersonSearch(self.refId)
		person_search.scope = PersonSearch.ScopeLocalValue
		person_search.me = "true"        
		person_return = self.getResponseForRequest(person_search)
		person_ = person_return["properties"]["results"]
		mecard = PersonSnippet(persons=person_)
		view = AddViews(self.refId, dialogPhase="Completion")		
		view.views = [mecard]
		self.sendRequestWithoutAnswer(view)
		self.complete_request()