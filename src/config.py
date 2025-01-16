from dataclasses import dataclass, asdict
from typing import Dict, Optional, List, Any



@dataclass
class urls:
    URL: "https://github.com/duplocloud/docs/tree/main/getting-started-1/application-focussed-interface"


@dataclass
class GithubMeta:
    name : str 
    path : str 
    sha : str 
    size : str 
    url :  str 
    html_url : str 
    git_url : str 
    download_url : str 
    type : str 
    _links : Dict[str, str]

    def to_dict(self) -> Dict[str, any]:
        return asdict(self)



@dataclass
class GithubData:
    meta : GithubMeta
    data : str 



class Chunk : 
    data : str 
    meta : GithubMeta

