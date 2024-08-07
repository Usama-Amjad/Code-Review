import warnings

warnings.filterwarnings("ignore")
from pprint import pprint
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser
from langchain_text_splitters import Language


def loader(filePath:str):
    file_ext = ['.py','.js','.cpp','.c','.java','.rs','.ts','.sc','.cs','.js','.kt','.rb']
    loader = GenericLoader.from_filesystem(
        filePath,
        glob="*",
        suffixes=file_ext,
        parser=LanguageParser(),
    )
    docs = loader.load()
    return docs[0].page_content
