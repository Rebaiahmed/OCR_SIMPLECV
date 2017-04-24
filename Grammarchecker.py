# -*- coding: utf-8 -*-
import grammar_check

tool = grammar_check.LanguageTool('en-GB')
text = 'La fidélisation des cliems dansum'
matches = tool.check(text)
print len(matches)
print grammar_check.correct(text, matches)
