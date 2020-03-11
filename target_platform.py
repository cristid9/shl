
PLATFORM_GOOGLE = "google_cloud"
PLATFORM_AWS = "amazon_cloud"
PLATFORM_AZURE = "microsoft_cloud"
PLATFORM_VMware = "vmware"

class TargetPlatform:
    """
    Data structure to model the cloud platform on which a 
    rule will be applied.
    """

    def __init__(self):
        self._platform_type = None
        self._project_name = None
        self._credentials = None
        self._service = None
        self._service_version = None

    @property
    def platform_type(self):
        return self._platform_type

    @platform_type.setter
    def platform_type(self, value):
        self._platform_type = value
    
    @property
    def project_name(self):
        return self._project_name

    @project_name.setter
    def project_name(self, value):
        self._project_name = value

    @property
    def credentials(self):
        return self._credentials

    @credentials.setter
    def credentials(self, value):
        self._credentials = value

    @property
    def project_version(self):
        return self._service_version

    @service_version.setter
    def service_version(self, value):
        self._service_version = value

    @property
    def service(self):
        return self._service

    @service.setter
    def service(self, value):
        self._service = value