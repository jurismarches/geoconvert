# -*- coding:utf-8 -*-
import re


class Address(object):
    """
    French address representation
    """
    def __init__(self, zipcode):
        self.zipcode = zipcode

        if zipcode is not None:
            self.zipcode_int = int(zipcode)

    def get_department(self):
        """
        Returns the department number from the zipcode
        """
        if self.zipcode is not None:
            dept_number = self.zipcode[:2]

            # Dom - Tom
            if int(dept_number) >= 97:
                dept_number = self.zipcode[:3]

            # Corse
            if dept_number == '20':
                if self.zipcode_int < 20190:
                    dept_number = '2A'
                else:
                    dept_number = '2B'

            return dept_number


class AddressParser(object):
    """
    Simple french address parser
    """
    address_class = Address
    zipcode_filters_re = [
        # Use \s before group because of words like "Publics", "Blancs"
        re.compile(r'\s(B\.?P\.?|C\.?S\.?|CEDEX)\s*\d*', flags=re.IGNORECASE | re.UNICODE)
    ]
    zipcode_re = re.compile(r'(?P<zipcode>\d{2}\s*?\d{2,3})')

    def _clean_address(self, address):
        """
        Returns filtered address
        """
        for regexp in self.zipcode_filters_re:
            address = regexp.sub('', address)
        return address

    def _parse_zipcode(self, address):
        """
        Tries to extract zipcode from address
        """
        match_list = list(self.zipcode_re.finditer(address))

        # It's easier to parse zipcode from the end of the string
        if match_list:
            return match_list[-1].group('zipcode').replace(' ', '').zfill(5)

    def get_address_class(self):
        """
        Returns address class
        """
        return self.address_class

    def parse(self, address):
        """
        Parses address and returns an Address object
        """
        address_class = self.get_address_class()
        cleaned_address = self._clean_address(address)
        zipcode = self._parse_zipcode(cleaned_address)

        if zipcode and zipcode.isdigit():
            return address_class(
                zipcode=zipcode)

        return address_class(
            zipcode=None)
