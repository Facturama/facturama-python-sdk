from . import BaseEndpointTestCase


class BranchOfficeEndpointTestCase(BaseEndpointTestCase):
    def test_branch_create(self):
        self.client._credentials = ('pruebas', 'pruebas2011')
        branch = self.client.Branch.create(self.branch_office_object.copy())
        print(branch['Id'])
        assert branch['Name'] == 'Corp Inc'

    def test_branch_get(self):
        self.client._credentials = ('pruebas', 'pruebas2011')
        branch = self.client.Branch.all()
        assert branch
