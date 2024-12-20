#解码网页请求

import requests


url = 'https://mooc1.chaoxing.com/mooc-ans/mooc2/work/dowork?courseId=244753507&classId=102435965&cpi=357813055&workId=37061678&answerId=53504334&standardEnc=c8785ddedc0674e49a7fff22e4b431a0&enc=6a2b69d92a20a39d3fe6e7341eaab1a9'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': 'https://mooc1.chaoxing.com/mooc2/work/list?courseId=244753507&classId=102435965&cpi=357813055&ut=s&enc=bf29108add537a592121bf9127328e89',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
    'Cookie' : 'lv=0; fid=42137; xxtenc=d0c1f1704bad96080f305a4b435f13d0; \
                createSiteSource=num8; wfwfid=42137; source=num2; workRoleBenchId=0; \
                siteType=2; wfwEnc=C9A1E0ABC647E455784B55D1BF980802; styleId=; spaceFid=42137; \
                spaceRoleId=""; k8s=1727167409.77.8855.378789; route=3cfd8ee391150acbf63626fecc6e7627; \
                thirdRegist=0; _uid=292519753; uf=d9387224d3a6095bdb1442936df0bec960c2f23cc4162e0ec2e7553734dace723c4\
                6fb4aaf4afcb85f53900694937525748a002894d7f44e88b83130e7eb47043d60939e5db592aa09c56e80afed835ed3d56c5\
                b6a42238d2ae74e9964a6bbd9b4233087bc1c99cdaa2ebad65cd196bb; _d=1728353274146; UID=292519753; vc=943\
                6E1BAAD091ECAC0FC3B18D6A25C27; vc2=85C808FF03C280B22533D31CD8811D48; vc3=ZkvqDqYS9QpZCWp9x%2Bt47CE\
                S9S3XcqMtDcDUN2RBcNaqXDb4DVJRGBbc1GFt3Yv7yzK8T%2BJhwAheZ1D%2Bl5vz8FqqbrhyNwKUFG%2BOSm5mwmhKI8gR6l\
                jTDQR6abhqX5vrhSPpJLkG8Nk3EBBSjRFTrMY95WvI6SsQDBOKJQAyV5s%3D91d9e8bc824ce7dd647a50c19aa72c62; cx_p\
                _token=5cb778ec6e5cbed6767eabe086123777; p_auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aW\
                QiOiIyOTI1MTk3NTMiLCJsb2dpblRpbWUiOjE3MjgzNTMyNzQxNDgsImV4cCI6MTcyODk1ODA3NH0.seN7NIMreoooxIrW8rAXdR\
                acuqF5BqVUA8vNJCMj4NM; DSSTASH_LOG=C_38-UN_2181-US_292519753-T_1728353274149; tl=1; jrose=FC3A9B5F\
                1E04CF1102D6527D21F20388.mooc-3131002049-wfmnz'

}

response = requests.get(url, headers=headers)
print(response.text)
