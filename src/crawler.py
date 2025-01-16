import requests
import json
from typing import Dict, Optional, List, Tuple,Iterator, Callable
from dataclasses import dataclass, asdict
from src.config import *



# class GithubCrawler():
#     def get_metadata(self, url:str) -> Iterator[GithubMeta]:
#         _, _, _, owner, repo, tree, branch, *path_parts = url.split('/')
#         api_url = f'"https://api.github.com/repos/{owner}/{repo}/contents/{'/'.join(path_parts)}?ref={branch}'
#         meta_data : GithubMeta= self._meta_data(api_url)
#         list_metadata = []
#         for item in meta_data:
#             if item.type == "dir":
#                 list_metadata+= self.get_metadata(item.html_url)
#             else:
#                 list_metadata+= [item]
#     def invoke(self):
#         urls_instance = urls(URL="https://github.com/duplocloud/docs/tree/main/getting-started-1/application-focussed-interface")
#         list_meta : Iterator(GithubMeta) = self.get_metadata(url=urls_instance.URL)
#         data : Iterator[Optional[GithubData]] = [self.get_metadata(meta_data) for meta_data in list_meta]


    
#     def _meta_data(self, api_url) -> Iterator[Optional[GithubMeta]]:
#         response = requests.get(api_url)
#         if response.status_code == 200:
#             json_out  = json.loads(response.text)
#             return [GithubMeta(**json_obj) for json_obj in json_out]
#         else:
#             return [] 
        
#     def download_data(self, meta_data: GithubMeta) -> Optional[GithubData]:
#         download_url  = meta_data.download_url
#         file_response = requests.get(download_url)
#         if file_response.status_code == 200:
#             # Chunk the document content
#             raw_text = file_response.text
#             return GithubData( meta=meta_data, data=raw_text)

#         else:
#             print(f"Failed to download {meta_data.name}. Status code: {file_response.status_code}")
#             return None 










class GitHubCrawler:
    def download_meta(self, url : str) -> Iterator[GithubMeta]:
        _, _, _, owner, repo, tree, branch, *path_parts = url.split('/')
        api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{'/'.join(path_parts)}?ref={branch}"
        meta_data : GithubMeta = self._meta_data(api_url)
        list_meta = []
        for item in meta_data:
            if item.type == 'dir':
                list_meta += self.download_meta(item.html_url)
            else:
                list_meta += [item]
        return list_meta 
    
    def invoke(self):
    
        urls_instance = urls(URL="https://github.com/duplocloud/docs/tree/main/getting-started-1/application-focussed-interface")
    
        list_meta : Iterator[GithubMeta] = self.download_meta(url =urls_instance.URL)        
        data      : Iterator[Optional[GithubData]] = [self.download_data(meta_data) for meta_data in list_meta]

        return data 

    
    def download_data(self, meta_data : GithubMeta) -> Optional[GithubData] :
        download_url  = meta_data.download_url
        file_response = requests.get(download_url)
        if file_response.status_code == 200:
            # Chunk the document content
            raw_text = file_response.text
            return GithubData( meta=meta_data, data=raw_text)

        else:
            print(f"Failed to download {meta_data.name}. Status code: {file_response.status_code}")
            return None 


    def _meta_data(self, api_url) -> Iterator[Optional[GithubMeta]]:
        response = requests.get(api_url)
        if response.status_code == 200:
            json_out  = json.loads(response.text)
            return [GithubMeta(**json_obj) for json_obj in json_out]
        else:
            return []  
        



