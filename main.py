import typer
from subfinder_recon.main import SubDomainReconTool
from httpx_tool.httpx_tool import ToolHTTPX
from scan_api import acunetix
app = typer.Typer()


@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")

@app.command()
def scan(url: str):
    arr = scanDomainTool(url)
    liveDomains = httpxTool(arr)
    acunetixTool(liveDomains)

def scanDomainTool(url: str):
    if len(url) == 0:
        print('Please enter a URL.')
        return
    tool = SubDomainReconTool(url)
    listSubDomain = tool.run()
    print(listSubDomain)
    return listSubDomain


def httpxTool(arr: list):
    tool = ToolHTTPX(arr)
    result = tool.enumerate_subdomains()
    print(result)
    return result


def acunetixTool(arr: list):
    for domain in arr: 
        id = acunetix.config(domain)
        print(id)

if __name__ == "__main__":
    app()