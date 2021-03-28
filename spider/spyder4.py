"""
爬取药监总局中的企业详情数据
url: http://app1.nmpa.gov.cn/data_nmpa/face3/base.jsp?tableId=25&tableName=TABLE25&title=%B9%FA%B2%FA%D2%A9%C6%B7&bcId=152904713761213296322795806604
需求:
    - 将首页中每一家企业的详情数据进行爬取(详情页对应的数据)
    - 将前2页的数据爬取即可
难点:
    - 用不到数据解析
    - 所有的数据都是动态加载出来的
提示:
    - 先试着将一家企业的详情页的详情数据爬取出来,然后再取爬取多家企业的数据
"""
import requests

url = '''http://app1.nmpa.gov.cn/data_nmpa/face3/c
ontent.jsp?6SQk6G2z=GBK-5FdYnTy_P1wTkI_e7bHrEPpkOi
rgubYpVdWo8N08ZZYpRv__hUKClw425M5.pxcz0cGC40sXGA69w
ISZYqx7riSrN60ka0A3RMXTZS6wgXenYeexJuSaFk0j3IbQ5pyQ
wH0SG1oGXCQG60S.nMZwjH4kWMMQUxVaiZ2vLS_Vb63yaZ5ixHe
GXK6RpBdKFoXrC8NHufZ7B2jWIerU2f1TKShPgD8YszFWf8j.yZ
eyHJqfnniMwN4lDNLh1cWV7JXHKI56Fk9VLJBQCJQ5WhqD3Rip_
j6NhWwjlfYIOP1DqErdki_iSN1aRFgwRrEa8TK4ctSRZVIMfOBD
dohyygEMSeRayFGul25D2cqecjgf4qWZ&c1SoYK0a=GBK-4P6b1
zVniacOL83p8flggAkSHRqf3KGyxzEoSvFSZquZA6Ixpl4mvF0i
XMW3GYyN_RFt3WSW7UaaWr75ujpiiKyHPjaeyRzTi66P7UnBfab
JKGpNmak74v8KmqeyL7t6JlcDBF2PCI6mcxezkoFAir9Rsbhs59
VobapfmmBW27h4Ie3sM0fZmnvgx62aAbnHACcXKgCZRJDNPWGBIhewlxa'''

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chro'
                  'me/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'
}

params = {
    '6SQk6G2z': 'GBK-5v9ZdwBSkSF_3EfHue516xz24pC77NqAZn6poiAMs'
                'v7eMaD1BHSvjX4JlWCLDDfwgxOa4M4_40uVfjATC63guj'
                'BgCUs6S5M3IFU.sLY4mEh0C2oX8Jm2ihkHyBnhytj6ThT'
                '8Dwqa.KeItaHcxO98p5gWIisn1.qzzswYs9Iq8AiiYXn8'
                'AmA.A13FlvYMn1EJqafDSdzNbQHFo9FOxc7RafnmLDRw.'
                'WtJiEREKaIYeEE3o6TGh11NynpW1vWjBBY5fie0YLfmRUK'
                'Fh9yZSj2IpBHYRRCfU7n5dCtEOMUpD1IxQM3gu0LLD9LCE'
                'YaMelncpwzppfGAtRGGNkC9tb5MCfdEgW67uWm47qc.LpBaw0Ba',
    'c1SoYK0a': 'GBK-4p62U_y6bcBf6MNzMer7aHtTVlq1QVO1vg_rsJt5X'
                'DKqs.ZpbuvyjKDGDMJPwAEam3UBg19mDJrksoXqV20wj2'
                'r5mAIOB7s1VfwsOgkWOKxTi_d3UDEuUzzRS4SYn.QKKQz'
                'ISWBcfdGcLusb.FNvelbCRa2IkavlAbPedTAGamtUyp2E'
                'zAWmdK.nwBpZ0S0zEBr4uvhQL93RPqEwHK3Y2AA'
}

response = requests.get(url=url, params=params, headers=headers)
page_text = response.text
print(page_text)
