from fastapi import FastAPI, HTTPException, Header, Body
from fastapi.responses import Response
from pydantic import BaseModel
import xmltodict



app = FastAPI()




class XMLData(BaseModel):
    xml: str




db = [{'uid': '999941057058','name': 'Shivshankar Choudhury','dob': '13-05-1968','dobt': 'V','gender': 'M','phone': '2810806979','email': 'sschoudhury@dummyemail.com','street': '12 Maulana Azad Marg','vtc': 'New Delhi','subdist': 'New Delhi','district': 'New Delhi','state': 'New Delhi','pincode': '110002'},
        {'uid': '999971658847','name': 'Kumar Agarwal','dob': '04-05-1978','dobt': 'A','gender': 'M','phone': '2314475929','email': 'kma@mailserver.com','building': 'IPP, IAP','landmark': 'Opp RSEB Window','street': '5A Madhuban','locality': 'Veera Desai Road','vtc': 'Udaipur','district': 'Udaipur','state': 'Rajasthan','pincode': '313001'},
        {'uid': '999933119405','name': 'Fatima Bedi','dob': '30-07-1943','dobt': 'A','gender': 'F','phone': '2837032088','email': 'bedi2020@mailserver.com','building': 'K-3A Rampur Garden','vtc': 'Bareilly','district': 'Bareilly','state': 'Uttar Pradesh','pincode': '243001'},
        {'uid': '999955183433','name': 'Rohit Pandey','dob': '08-07-1985','dobt': 'A','gender': 'M','phone': '2821096353','email': 'rpandey@mailserver.com','building': '603/4 Vindyachal','street': '7TH Road Raja Wadi','locality': 'Neelkanth Valley','poname': 'Ghatkopar (EAST)','vtc': 'Mumbai','district': 'Mumbai','state': 'Maharashtra','pincode': '243001'},
        {'uid': '999990501894','name': 'Anisha Jay Kapoor','gender': 'F','dob': '01-01-1982','dobt': 'V','building': '2B 203','street': '14 Main Road','locality': 'Jayanagar','district': 'Bangalore','state': 'Karnataka','pincode': '560036'}
]
ret = 'n'




@app.get("/test/")
async def auth(xml_data: XMLData = Body(..., media_type="application/xml")):
    
    
    xml_input = xml_data.xml
    print(xml_input)
               
    
    xml_response = '''<AuthRes ret="n" code="" txn="" err="" ts="" actn="" info="">
    <BfdRanks>
    </BfdRanks>
    <Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
        <SignedInfo>
            <CanonicalizationMethodAlgorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315" />
            <SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsasha256" />
            <Reference URI="http://127.0.0.1:8000/2.5/public/9/9/MCNYL7FpPgjEhx7HBp9tu59Vdm4FnYGlxuqHctfAeNNaCufVafshqzQ/">
                <Transforms>
                    <Transforlgorithm="http://www.w3.org/2000/09/xmldsig#envelopedsignature" />
                </Transforms>
                <DigestMethodAlgorithm="http://www.w3.org/2000/09/xmldsig#sha256"/>
                <DigestValue></DigestValue>
            </Reference>
        </SignedInfo>
        <SignatureValue></SignatureValue>
    </Signature>
</AuthRes>'''

    response = Response(content=xml_response, media_type="application/xml")
    return xml_response