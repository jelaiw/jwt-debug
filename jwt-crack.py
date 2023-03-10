import sys
import hmac
import base64

assert len(sys.argv) == 2
jwt = sys.argv[1]
print(jwt)

DELIMITER = '.'
words = jwt.split(DELIMITER)
assert len(words) == 3

print(words[2]) # Print signature for debugging.

data = words[0] + DELIMITER + words[1]
# See https://stackoverflow.com/a/43882903.
# Note comment125847252_43882903.
data = data.encode() # Default UTF-8 byte encoding.

key = b'crapi'
digest = hmac.new(key, msg=data, digestmod='sha256').digest()
# Remove padding as described at https://www.rfc-editor.org/rfc/rfc7515.
tag = base64.urlsafe_b64encode(digest).rstrip(b'=')
tag = tag.decode() # Decode UTF-8 encoded bytes.

print(words[2] == tag)
