# -*- coding: utf-8 -*

import re

from expects import *
from expects.testing import failure


with describe('match'):
    with before.all:
        self.str = 'My foo string'

    with it('should pass if string matches expected regexp'):
        expect(self.str).to(match(r'My \w+ string'))

    with it('should pass if string matches expected regexp with re flags'):
        expect(self.str).to(match(r'my [A-Z]+ strinG', re.I))

    with it('should fail if string does not match expected regexp'):
        with failure("to match 'My \\\\W+ string'"):
            expect(self.str).to(match(r'My \W+ string'))

    with context('#negated'):
        with it('should pass if string does not match expected regexp'):
            expect(self.str).not_to(match(r'My \W+ string'))

        with it('should pass if string does not match expected regexp with re flags'):
            expect(self.str).not_to(match(r'My \W+ string', re.I))

        with it('should fail if string matches expected regexp'):
            with failure("not to match 'My \\\\w+ string'"):
                expect(self.str).not_to(match(r'My \w+ string'))