import requests

# 发送GET请求
print("GET请求:")
response = requests.get("https://httpbin.org/get")
print(f"状态码: {response.status_code}")
print(f"响应头: {dict(response.headers)}")

# 发送POST请求
print("\nPOST请求:")
data = {"username": "test", "password": "123456"}
response = requests.post("https://httpbin.org/post", data=data)
print(f"状态码: {response.status_code}")
print(f"表单数据: {response.json()['form']}")

# 带参数的请求
print("\n带参数的请求:")
params = {"q": "python", "page": 1}
response = requests.get("https://httpbin.org/get", params=params)
print(f"完整URL: {response.url}")

# 处理JSON响应
print("\nJSON响应:")
response = requests.get("https://httpbin.org/json")
data = response.json()
print(f"标题: {data['slideshow']['title']}")
