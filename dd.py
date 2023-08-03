import requests

headers = {
    # Already added when you pass json= but not when you pass data=
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}

json_data = '{"articles": [{"link": "https://blogs.juniper.net/en-us/threat-research/new-pastebin-like-service-used-in-multiple-malware-campaigns", "title": "New pastebin-like service used in multiple malware campaigns | Official Juniper Networks Blogs", "description": "Juniper Threat Labs identified several malware campaigns that rely on a pastebin-like service for its infection chain. The domain in question is paste.nrecom.net. The attacks usually start as a phishing email and, when a user is tricked into executing the malware, it downloads the succeeding stage of the malware from paste.nrecom.net and loads it into the memory without writing to disk.", "img": "https://blogs.juniper.net/wp-content/uploads/2020/10/SEC-200652-_DIGITAL_Threat-Labs-Blog-image-for-Pastebin-Malware.gif"}, {"link": "https://linear.app/blog/settings-are-not-a-design-failure", "title": "Settings are not a design failure", "description": "The systematic thinking in our industry is that settings are the result of design failure. As designers, our goal is to create product experiences that don\u2019t require any adjustment by the user. So offering customization options is often seen as a failure to make firm product decisions. I think there is a misunderstanding about what settings really are.", "img": "https://cdn.sanity.io/images/ornj730p/production/2bc44b5d1f38437b5a9fd4392b4473cf38174d10-2400x1200.png"}], "youtube": []}'
response = requests.post('https://jsonblob.com/api/jsonBlob', headers=headers, json=json_data)

print(response.headers)