import cloudconvert

from envs import CLOUD_KEY


class PdfConverter:
    def __init__(self, key=CLOUD_KEY, input_format="pdf", output_format="epub"):
        self.converter = cloudconvert.Api(CLOUD_KEY)
        self.process = self.converter.createProcess({
            "inputformat": "pdf",
            "outputformat": "epub"
        })
    
    def convert_to_epub(self, file_url):
        short_link_to_converted_file = self.__convert_file(file_url)
        full_link_to_converted_file = f'https:{short_link_to_converted_file}'
        return full_link_to_converted_file
        
    def __convert_file(self, file_url, output_format="epub"):
        self.process.start({
            "input": "download",
            "file": file_url,
            "outputformat": output_format,
        })
        self.process.wait()
        converted_file_url = self.process.data["output"]["url"]
        return converted_file_url