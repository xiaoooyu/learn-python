import sys
import os

print "Hello World!"
# print "Hello Again"
# print "I like typing this"
# print "This is fun."
# print 'Yay! Printing.'
# print "I'd much rather you 'not'."
# print 'I "said" do not touch this.'
# print 'This is another line'


ALLOWED_FILE_MIMETYPE = {
    ".plist": "application/x-plist",
    ".ipa": "application/octet-stream",
    ".html": "text/html",
    ".png": "image/png",
    ".ver": "plain/text",
    ".apk": "application/vnd.android.package-archive"
}

print ALLOWED_FILE_MIMETYPE.has_key(".abc")
print ALLOWED_FILE_MIMETYPE.has_key(".html")

if ALLOWED_FILE_MIMETYPE.has_key(".html"):
	print "YES"

for file in os.listdir("."):
	
	fileName = os.path.basename(file)
	print fileName

	name, ext = os.path.splitext(file)
	print name, ext
