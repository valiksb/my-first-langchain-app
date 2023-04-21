# my-first-langchain-app
Activate your conda environment, in my case *my-first-langchain-app*
```shell
conda activate my-first-langchain-app
```
I got an error because with the certs 
```
Collecting package metadata (current_repodata.json): failed

CondaSSLError: Encountered an SSL error. Most likely a certificate verification issue.

Exception: HTTPSConnectionPool(host='conda.anaconda.org', port=443): Max retries exceeded with url: /conda-forge/osx-64/current_repodata.json (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)')))`
```
when I tried
https://python.langchain.com/en/latest/getting_started/getting_started.html#installation
```shell
conda install langchain -c conda-forge
```
To solve this issue I followed these steps on My Mac (thanks to folks that provide a solution, https://stackoverflow.com/questions/39356413/how-to-add-a-custom-ca-root-certificate-to-the-ca-store-used-by-pip-in-windows)
0.
```shell
python -m pip install truststore
```
1.
```shell
echo quit | openssl s_client -showcerts -servername "curl.haxx.se" -connect curl.haxx.se:443 > cacert.pem
```
2.
```shell
mkdir ~/mycerts
```
3.
```shell
mv cacert.pem ~/mycerts/ca-bundle.crt
```
4.
```shell
pip config set global.cert ~/mycerts/ca-bundle.crt
```
5.
```shell
conda config --set ssl_verify ~/mycerts/ca-bundle.crt
```
6.
```shell
pip config list
conda config --show ssl_verify
```
7. try again
```shell
conda install langchain -c conda-forge
```
If the above does not solve the problem, you CAN disable ssl_verify, which I would NOT recommend, UNLESS you are sure
where you are downloading/installing stuff from
8. OPTIONAL STEP IF THE ABOVE 6. steps dont work
```shell
conda config --set ssl_verify false
```
try again step 7. and then enable ssl_verify (step 5.)
```shell
conda config --set ssl_verify ~/mycerts/ca-bundle.crt
```

