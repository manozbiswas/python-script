from __future__ import print_function
import itertools
import os


# Specify the separator of the block
def isa_group_separator(line):
    return line == '\n'


# return a writing directory
def get_the_directory():
    # give the file path to write the files
    path = os.path.dirname(__file__)
    path = path + "/files/"
    if not os.path.exists(path):
        os.makedirs(path)
    return path


# give the file path from where you want to read the file
def main_module(i=1):
    path = os.path.dirname(__file__)
    with open(path + "/html.txt") as f:
        for key, group in itertools.groupby(f, isa_group_separator):
            if key == False:
                with open(get_the_directory() + str(i) + ".html", 'w') as d:
                    d.writelines(group)
                    d.close()
                    i += 1
    f.close()

# call the function
main_module()

#####################################

 input file: html.text or html.html
 
 <!DOCTYPE html>
<html>
<!-- start Mixpanel --><script type="text/javascript">(function(e,b){if(!b.__SV){var a,f,i,g;window.mixpanel=b;b._i=[];b.init=function(a,e,d){function f(b,h){var a=h.split(".");2==a.length&&(b=b[a[0]],h=a[1]);b[h]=function(){b.push([h].concat(Array.prototype.slice.call(arguments,0)))}}var c=b;"undefined"!==typeof d?c=b[d]=[]:d="mixpanel";c.people=c.people||[];c.toString=function(b){var a="mixpanel";"mixpanel"!==d&&(a+="."+d);b||(a+=" (stub)");return a};c.people.toString=function(){return c.toString(1)+".people (stub)"};i="disable time_event track track_pageview track_links track_forms register register_once alias unregister identify name_tag set_config people.set people.set_once people.increment people.append people.union people.track_charge people.clear_charges people.delete_user".split(" ");
for(g=0;g<i.length;g++)f(c,i[g]);b._i.push([a,e,d])};b.__SV=1.2;a=e.createElement("script");a.type="text/javascript";a.async=!0;a.src="undefined"!==typeof MIXPANEL_CUSTOM_LIB_URL?MIXPANEL_CUSTOM_LIB_URL:"file:"===e.location.protocol&&"//cdn.mxpnl.com/libs/mixpanel-2-latest.min.js".match(/^\/\//)?"https://cdn.mxpnl.com/libs/mixpanel-2-latest.min.js":"//cdn.mxpnl.com/libs/mixpanel-2-latest.min.js";f=e.getElementsByTagName("script")[0];f.parentNode.insertBefore(a,f)}})(document,window.mixpanel||[]);
mixpanel.init("395a197b2ff48f4c033c1b15a4f4ffad");</script><!-- end Mixpanel -->
<head>
  <title>Max's Simple Webpage</title>
</head>
<body>
  This is a page 1
</body>
<script type="text/javascript">
    mixpanel.track("Fetch", {"time": "1454789572","distinct_id": "B00155","ip": "66.249.84.241","Browser": "Chrome","Operating System": "Windows 7","User Type": "Anonymous","Client Type": "Desktop","Action Type": "View","Page Type": "Help" });
</script>
</html>

<!DOCTYPE html>
<html>
<!-- start Mixpanel --><script type="text/javascript">(function(e,b){if(!b.__SV){var a,f,i,g;window.mixpanel=b;b._i=[];b.init=function(a,e,d){function f(b,h){var a=h.split(".");2==a.length&&(b=b[a[0]],h=a[1]);b[h]=function(){b.push([h].concat(Array.prototype.slice.call(arguments,0)))}}var c=b;"undefined"!==typeof d?c=b[d]=[]:d="mixpanel";c.people=c.people||[];c.toString=function(b){var a="mixpanel";"mixpanel"!==d&&(a+="."+d);b||(a+=" (stub)");return a};c.people.toString=function(){return c.toString(1)+".people (stub)"};i="disable time_event track track_pageview track_links track_forms register register_once alias unregister identify name_tag set_config people.set people.set_once people.increment people.append people.union people.track_charge people.clear_charges people.delete_user".split(" ");
for(g=0;g<i.length;g++)f(c,i[g]);b._i.push([a,e,d])};b.__SV=1.2;a=e.createElement("script");a.type="text/javascript";a.async=!0;a.src="undefined"!==typeof MIXPANEL_CUSTOM_LIB_URL?MIXPANEL_CUSTOM_LIB_URL:"file:"===e.location.protocol&&"//cdn.mxpnl.com/libs/mixpanel-2-latest.min.js".match(/^\/\//)?"https://cdn.mxpnl.com/libs/mixpanel-2-latest.min.js":"//cdn.mxpnl.com/libs/mixpanel-2-latest.min.js";f=e.getElementsByTagName("script")[0];f.parentNode.insertBefore(a,f)}})(document,window.mixpanel||[]);
mixpanel.init("395a197b2ff48f4c033c1b15a4f4ffad");</script><!-- end Mixpanel -->
<head>
  <title>Max's Simple Webpage</title>
</head>
<body>
  This is a page 2
</body>
<script type="text/javascript">
    mixpanel.track("Fetch", {"time": "1454814521","distinct_id": "B00102","ip": "205.225.241.126","Browser": "Firefox","Operating System": "Windows 7","User Type": "Anonymous","Client Type": "Desktop","Action Type": "Upload","Page Type": "Document" });
</script>
</html>


##################

Output:
1.html
2.html

