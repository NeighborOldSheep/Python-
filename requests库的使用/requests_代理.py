import requests 

url = 'https://www.baidu.com/s?'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'Cookie': 'BIDUPSID=C836E305942F799937F00A58BFA59684; PSTM=1614649691; __yjs_duid=1_98d6029be6aa0aadf40b5785eddd84ff1620352921273; ZFY=xRV4tptAOgP4:BW5vVyDq3EPbSyp5X3:BaRo822OMvkEs:C; __bid_n=183f90655c4a8f6ad64207; FEID=v10-1d2325ff78a4f5149646c35600764bfe07ce9133; BAIDU_WISE_UID=wapp_1670829621868_890; __xaf_fpstarttimer__=1672691579691; __xaf_thstime__=1672691580415; __xaf_fptokentimer__=1672691580535; BAIDUID=0A89E676F0CA7F3AE5E217EA2F2B627B:FG=1; BAIDUID_BFESS=0A89E676F0CA7F3AE5E217EA2F2B627B:FG=1; COOKIE_SESSION=0_1_1_1_1_3_1_0_1_1_16_0_0_0_23_3_1676175958_1676175938_1676175935%7C1%230_1_1676175935%7C1; RT="z=1&dm=baidu.com&si=5925256a-a569-4634-ae8c-f6d0d939b9c8&ss=lex6f5na&sl=0&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ul=4wu&hd=4z2"; BD_UPN=12314753; B64_BOT=1; H_WISE_SIDS=219946_219623_234020_216840_213361_229966_214795_219943_213034_230181_204919_230288_241714_242158_242311_242489_238267_110085_227870_236308_243706_243877_244416_232628_244723_240590_244957_244267_245274_245412_245700_242430_246466_246491_242682_246177_234296_234208_246583_246855_247050_247224_245042_245540_247355_247391_247632_247799_243424_242266_236536_248075_243657_248147_248512_248480_248471_248608_248645_245895_248726_247629_249016_247584_249180_107312_248312_248866_249529_249531_249605_248903_248124_249764_248156_244281_249922_249908_249983_249123_245920_246093_250181_250123_250164_248718_248331_247551_8000077_8000101_8000116_8000126_8000137_8000155_8000163_8000167_8000177_8000186_8000189; H_WISE_SIDS_BFESS=219946_219623_234020_216840_213361_229966_214795_219943_213034_230181_204919_230288_241714_242158_242311_242489_238267_110085_227870_236308_243706_243877_244416_232628_244723_240590_244957_244267_245274_245412_245700_242430_246466_246491_242682_246177_234296_234208_246583_246855_247050_247224_245042_245540_247355_247391_247632_247799_243424_242266_236536_248075_243657_248147_248512_248480_248471_248608_248645_245895_248726_247629_249016_247584_249180_107312_248312_248866_249529_249531_249605_248903_248124_249764_248156_244281_249922_249908_249983_249123_245920_246093_250181_250123_250164_248718_248331_247551_8000077_8000101_8000116_8000126_8000137_8000155_8000163_8000167_8000177_8000186_8000189; FPTOKEN=hIFtOzXgL7V4U6cIc7zeO60dihrtj15Ww5lsW1TnrmapoC6FbvOC5tItnEppDra/GUtiqrVlmxBcGdEIzrGKq3WQiZZ/nUZhxOvIJCLSYZT4r1jqL2fg/5MlYXiILE+bG7FA55JYx4moEvreagPvT6OywmtARbsKYEbTC98YFYucCCAVmal/cuLHxPVHvsh6bz/mtG8+Qf3QzDt0mFjai8GQcq+avNYXN3+XVbNIk1V+MjROjIz5T4089GI2Y45MTkDavykBYbhC0Ovn729vdMwph6MDttXuDrhqnyj7va5D9lQ1Jz0LF8CDJlf0vgfjQ6g49wVxKWwpH15e/FqoQGRsv5shCJxbyzUms3CN55yK5KBOY4Ga0e8v3pdaT5fAs/vFyZp+DF8LSgWza1OoWA==|OBwiARbcOaAYGgA9JVqhbIfKVCvOmXbLCvDB++lbotQ=|10|ab0ccdf77c41209d9f4d24622524c7a2; BD_HOME=1; BA_HECTOR=2025a40lag242k20ag2hag611i0ka6e1n; BD_CK_SAM=1; PSINO=7; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; H_PS_645EC=c083X8KZ6tG2VLpGOkUrnq%2Bi14Z5tgakXlQpNtGqICCD4NycN4Ct6FLFBwY; baikeVisitId=e01df7cb-215c-4b8a-a720-bc1e6a593562; ab_sr=1.0.1_YTdiNDc3NWUwN2IzMDljZjM2NmIwMGFiNmZjOTA3YWMzMjk3ZWRmOWVhYTM2YWNmNjU4NTMyZWZlZmExMGUyYmYxYjQ1M2M0NmFlZGIyZmY3ZWU5MzU2Yjk0ZTExNWQwYzQyNDZkMzA4MGNmYTJkZWUxYzk1ZDYyNDliMzNiYWI0NzgzZTEwNGY0Mzc3YWYxYWRmYWE5MTY0ZGRhMDgwNA==; BDUSS=mhWY1Qyc05SRzluQWJHVFpHZU1tUVE4cm94TmFOWX4wRk4xdHZsbG1halh2REZrSUFBQUFBJCQAAAAAAAAAAAEAAAC1syDxuPSx2uzhwM~R7nRlbAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANcvCmTXLwpkc; BDUSS_BFESS=mhWY1Qyc05SRzluQWJHVFpHZU1tUVE4cm94TmFOWX4wRk4xdHZsbG1halh2REZrSUFBQUFBJCQAAAAAAAAAAAEAAAC1syDxuPSx2uzhwM~R7nRlbAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANcvCmTXLwpkc; H_PS_PSSID=38185_36542_38132_37861_38170_38290_38231_36803_37937_38312_38322_38041_26350_38282_37881',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
}

data = {
    'wd' : 'ip'
}

proxy = {
    'http' : '121.13.252.62:41564',
    'http' : '27.42.168.46:55481'
}




response = requests.get(url=url,params=data,headers=headers,proxies=proxy)
response.encoding = 'utf-8'
content = response.text 
#print(content)

with open('daili.html','w',encoding='utf-8') as f:
    f.write(content)