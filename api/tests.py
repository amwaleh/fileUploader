from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase
from django.core.files import File
import mock


class TestImportViewsets(APITestCase):
    def test_upload_with_wrong_key(self):
        file_mock = mock.MagicMock(spec=File, name='FileMock')
        Data = {
                'title': 'sample',
                'File': file_mock,
                }
        response = self.client.post ('/file', Data)
        self.assertEqual(response.status_code,301)