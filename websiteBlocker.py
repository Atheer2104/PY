import appscript

# we get twodimensional array inside is another containg the current active urls
# we unpacking the array by [urls] this will unpack the outer most array
# and just leave us with one dimesnional array containing the urls
[urls] = appscript.app('Safari').windows.tabs.URL()


# appscript.app("Safari").windows.tabs[1].close()
# close all tabs
# appscript.app("Safari").windows.tabs.close()

blockedUrls = ["https://www.youtube.com"]
while True:
    index = 0
    for url in urls:
        for blockedUrl in blockedUrls:
            # checking if a url from the blockedurls is one of the active url of our browser
            if blockedUrl in url:
                # it means there is a url that we should block
                # getting the index of the element so we can know what window to clso
                index = urls.index(url) + 1


    appscript.app("Safari").windows.tabs[index].close()


