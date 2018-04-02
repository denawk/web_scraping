# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 07:54:06 2018

@author: Evan Kwan
"""
added by ekwan apr 1 2018
2nd added by ekwan apr 1 2018
3rd added by ekwan apr 1 2018
4th added by ekwan apr 1 2018
5th added by ekwan apr 1 2018
6th added by ekwan apr 1 2018
7th
8th
9th
10th

keywords = input("Please enter the things you want to see in a recipe: ")

url = "http://www.epicurious.com/search/" + keywords
response = requests.get(url)

if response.status_code == 200:
    print("Success")
else:
    print("Failure")
###################################


# url = "https://en.wikipedia.org/wiki/main_page"
url = 'https://www.ratemyteachers.com/hunter-college-high-school/25767-s'

# The rest of your code should go below this line
import requests

# make html request, get the html response and store it
hchs_resp = requests.get(url)

# check the html response status code for 200
hchs_resp.status_code
# 200

# decode the (byte string) html response with unicode 'utf-8'
# and store as python string in variable wiki_text
hchs_text = hchs_resp.content.decode("utf-8")

type(hchs_resp)
# requests.models.Response

type(hchs_text)
# str

hchs_text


# import requests
from bs4 import BeautifulSoup

results_page = BeautifulSoup(hchs_resp.content,'lxml')
print(results_page.prettify())




####################################



# search string for "Did you know" and get location number
# of first match
hchs_text.find("")
# 13605
# at byte 13,605.

# return text at location...
hchs_text[13600:13650]
# '...">Did you know...</span></h2>\n<div id="mp-dyk" '


########################



def get_recipes(keywords):
    recipe_list=list()
    
    import requests
    from bs4 import BeautifulSoup

    url = "http://www.epicurious.com/search/" + keywords
    response = requests.get(url)
    
    # better to use a try/except to catch errors, but here use if not then (no else)
    if not response.status_code == 200:
        # return a list eventhough it is empty
        return recipe_list
        # this ends the function call because nothing is performed after a return statement

    # continue from above if statement if false
    try:
        # specify parser "lxml"
        results_page = BeautifulSoup(response.content, "lxml")
        recipes = results_page.find_all('article', class_="recipe-content-card")
#        print(recipes)
        for recipe in recipes:
            recipe_name = recipe.find('a').get_text()
            recipe_link = "http://www.epicurious.com" + recipe.find('a').get('href')
            print(recipe_name, recipe_link)
            
    except:
        return recipe_list
    
    # if above return statements were not run,
    # run this return to return a value
    return recipe_list






########################


# So let's look at the
# BeautifulSoup functions we can use.

# <tag>.find(<tag_name>, attribute=value)       finds the first matching child tag (recursively)
# <tag>.find_all(<tag_name>, attribute=value)   finds all matching child tages (recursively)
# <tag>.get_text()                              returns the marketd up text
# <tag>.parent                                  returns the (immediate) parent
# <tag>.parents                                 returns all parents (recursively)
# <tag>.children                                returns the (direct) children
# <tag>.descendants                             returns all children (recursively)
# <tag>.get(attribute)                          returns the value of the specified attribute


# And there are many, many functions that you can use,
# but we're really interested mainly in
#    four of them.


# The 4 that we're interested in are
#    find,
#    find all,
#    get text, and
#    get attribute.

# You can also
#    navigate up and down your tree, using these four functions,
#        parents,
#        parents,
#        children, and
#        descendants.
# Would be one variable those for our class here.

# We look at just these four.




#########
#
# find_all finds all instances of a specified tag
# returns a result_set (a list)



all_a_tags = results_page.find_all('a')
for a_tag in all_a_tags:
    print(a_tag.get('href'))
'''
...
/howard-adams/2074712-t
/hunter-college-high-school/25767-s/physical-education
/howard-adams/2074712-t
/howard-adams/2074712-t
/eve-eisenstadt/246828-t
/hunter-college-high-school/25767-s/visual-arts
/eve-eisenstadt/246828-t
/eve-eisenstadt/246828-t
/kelly-honerkamp/7898685-t
/hunter-college-high-school/25767-s/math
/kelly-honerkamp/7898685-t
/kelly-honerkamp/7898685-t
...
'''




all_a_tags_btn = results_page.find_all('a', class_='btn view_more')
type(all_a_tags_btn)
all_a_tags_btn

teacher_list=[]
for a_tag_btn in all_a_tags_btn:
#    print(a_tag.get('href'))
    teacher_list.append('https://www.ratemyteachers.com' + a_tag_btn.get('href'))
teacher_list
['https://www.ratemyteachers.com/david-towber/172358-t',
 'https://www.ratemyteachers.com/drew-adams/1078417-t',
 'https://www.ratemyteachers.com/tom-scott/225880-t',
 'https://www.ratemyteachers.com/micheline-beaudry/239022-t',
 'https://www.ratemyteachers.com/peter-melman/1747652-t',
 'https://www.ratemyteachers.com/ben-morgenroth/3983117-t',
 'https://www.ratemyteachers.com/eliza-kuberska/193595-t',
 'https://www.ratemyteachers.com/bradley-scalise/7918595-t',
 'https://www.ratemyteachers.com/larry-ling/237643-t',
 'https://www.ratemyteachers.com/richard-fulco/1104609-t',
 'https://www.ratemyteachers.com/elizabeth-fox/231055-t',
 'https://www.ratemyteachers.com/tony-fisher/1681402-t',
 'https://www.ratemyteachers.com/steve-borowka/1655713-t',
 'https://www.ratemyteachers.com/margaret-sturiano/1371640-t',
 'https://www.ratemyteachers.com/sylvia-schaindlin/242184-t',
 'https://www.ratemyteachers.com/luke-batson/1352298-t',
 'https://www.ratemyteachers.com/linda-aboody/193569-t',
 'https://www.ratemyteachers.com/lourdie-castillo/7911689-t',
 'https://www.ratemyteachers.com/gregory-boyle/248077-t',
 'https://www.ratemyteachers.com/caitlin-samuel/3993811-t',
 'https://www.ratemyteachers.com/kasumi-parker/2146288-t',
 'https://www.ratemyteachers.com/michael-keleher/7911691-t',
 'https://www.ratemyteachers.com/audrey-maurer/2493647-t',
 'https://www.ratemyteachers.com/olivia-byun/8057509-t',
 'https://www.ratemyteachers.com/daniel-sangermano/682137-t',
 'https://www.ratemyteachers.com/carol-samuel/1376051-t',
 'https://www.ratemyteachers.com/claire-mazzola/193564-t',
 'https://www.ratemyteachers.com/satinder-jawanda/826502-t',
 'https://www.ratemyteachers.com/nikki-weinstein/1652812-t',
 'https://www.ratemyteachers.com/stacy-goldstein/1643756-t',
 'https://www.ratemyteachers.com/amelia-betancourt/1643770-t',
 'https://www.ratemyteachers.com/michael-stratechuk/234440-t',
 'https://www.ratemyteachers.com/roni-mistriel/242967-t',
 'https://www.ratemyteachers.com/brian-park/1683905-t',
 'https://www.ratemyteachers.com/kip-zegers/246707-t',
 'https://www.ratemyteachers.com/melissa-chapnick/1353338-t',
 'https://www.ratemyteachers.com/sarah-fogelman/486096-t',
 'https://www.ratemyteachers.com/jana-lucash/271302-t',
 'https://www.ratemyteachers.com/sheila-garcia/312565-t',
 'https://www.ratemyteachers.com/rembert-herbert/211443-t',
 'https://www.ratemyteachers.com/martha-curtis/234435-t',
 'https://www.ratemyteachers.com/lillian-drvostep/229540-t',
 'https://www.ratemyteachers.com/constance-rich/193686-t',
 'https://www.ratemyteachers.com/irving-kagan/234414-t',
 'https://www.ratemyteachers.com/betty-kleinfeld/323464-t',
 'https://www.ratemyteachers.com/david-joffe/1340051-t',
 'https://www.ratemyteachers.com/rebecca-hollander/234520-t',
 'https://www.ratemyteachers.com/sheila-krilov/234397-t',
 'https://www.ratemyteachers.com/bob-gaudenzi/244030-t',
 'https://www.ratemyteachers.com/christopher-unruh/529880-t',
 'https://www.ratemyteachers.com/ray-kaniatyn/242188-t',
 'https://www.ratemyteachers.com/thomas-keenan/478475-t',
 'https://www.ratemyteachers.com/clare-kudera/232426-t',
 'https://www.ratemyteachers.com/rebecca-ramirez/1638618-t',
 'https://www.ratemyteachers.com/richard-roundy/224414-t',
 'https://www.ratemyteachers.com/tara-foley/1714190-t',
 'https://www.ratemyteachers.com/hal-weinstein/316663-t',
 'https://www.ratemyteachers.com/rachel-basker/246734-t',
 'https://www.ratemyteachers.com/christina-moore/1032723-t',
 'https://www.ratemyteachers.com/ann-slavin/242978-t',
 'https://www.ratemyteachers.com/johnson-wong/1479620-t',
 'https://www.ratemyteachers.com/julie-reifer/239002-t',
 'https://www.ratemyteachers.com/joanne-roque/246855-t',
 'https://www.ratemyteachers.com/sewell/1054170-t',
 'https://www.ratemyteachers.com/jose-diaz/234507-t',
 'https://www.ratemyteachers.com/melanie-pflaum/1723216-t',
 'https://www.ratemyteachers.com/evanthia-basias/246866-t',
 'https://www.ratemyteachers.com/shannon-connors/1888882-t',
 'https://www.ratemyteachers.com/shawn-crouch/240689-t',
 'https://www.ratemyteachers.com/neil-potter/259598-t',
 'https://www.ratemyteachers.com/asumana-randolph/284663-t',
 'https://www.ratemyteachers.com/gilana-reiss/1895207-t',
 'https://www.ratemyteachers.com/justin-storer/1901835-t',
 'https://www.ratemyteachers.com/kimberly-airoldi/229532-t',
 'https://www.ratemyteachers.com/sue-monroe/317823-t',
 'https://www.ratemyteachers.com/emily-mines/7138025-t',
 'https://www.ratemyteachers.com/inalni-sharma/2406390-t',
 'https://www.ratemyteachers.com/lois-refkin/242625-t',
 'https://www.ratemyteachers.com/elaine-schwartz/225812-t',
 'https://www.ratemyteachers.com/steve-young/1906178-t',
 'https://www.ratemyteachers.com/sonya-mosco/240827-t',
 'https://www.ratemyteachers.com/yael-wyner/172356-t',
 'https://www.ratemyteachers.com/giovanna-termini/193565-t',
 'https://www.ratemyteachers.com/lori-jean-d-amico/172360-t',
 'https://www.ratemyteachers.com/richard-sasso/246652-t',
 'https://www.ratemyteachers.com/daniel-mozes/1922357-t',
 'https://www.ratemyteachers.com/michelle-rushforth/1923892-t',
 'https://www.ratemyteachers.com/sandra-miley/262028-t',
 'https://www.ratemyteachers.com/philip-frankel/1875164-t',
 'https://www.ratemyteachers.com/lee-weinberg/337869-t',
 'https://www.ratemyteachers.com/eugene-lim/1998685-t',
 'https://www.ratemyteachers.com/melinda-stepanski/1845470-t',
 'https://www.ratemyteachers.com/pamela-lewis/172355-t',
 'https://www.ratemyteachers.com/anthony-natelli/1960538-t',
 'https://www.ratemyteachers.com/wallace/239035-t',
 'https://www.ratemyteachers.com/carolyn-mayadas/264965-t',
 'https://www.ratemyteachers.com/bob-sabin/962015-t',
 'https://www.ratemyteachers.com/howard-adams/2074712-t',
 'https://www.ratemyteachers.com/eve-eisenstadt/246828-t',
 'https://www.ratemyteachers.com/kelly-honerkamp/7898685-t']


###################

'''
             <p class="comments">
              <span class="text" itemprop="description">
               he's scary sometimes as a teacher but when he visits us in Rosenberg's class.....he's fun. Me and my best friend call him Davie.
              </span>
             </p>
'''

teacher_dict={}
for i in range(len(teacher_list)):
# for i in range(1,2):
    comment_list=[]
    teacher_resp = requests.get(teacher_list[i])
#    teacher_text = teacher_resp.content.decode('utf-8')
    teacher_results_page = BeautifulSoup(teacher_resp.content,'lxml')
    all_span_tags = teacher_results_page.find_all('span', class_='text')
    for span in all_span_tags:
        comment_list.append(span.get_text().replace('\n',''))

    # split the url by '/', excluding this character, into a list and take index 3 list element
    name = re.split(r'(/)', teacher_list[i])[6]
    teacher_dict[name] = [teacher_list[i], comment_list]


teacher_dict['kelly-honerkamp']


####################




#####################
# teacher_list[0] - David Towber
<!DOCTYPE html>
<html>
 <head>
  <script type="text/javascript">
   (function(){
        window.beginTimeTrack = (new Date()).getTime();
      })();
  </script>
  <title>
   David Towber - Hunter College High School | RateMyTeachers
  </title>
  <meta content="IE=edge" http-equiv="X-UA-Compatible"/>
  <meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
  <script type="text/javascript">
   window.NREUM||(NREUM={});NREUM.info={"beacon":"bam.nr-data.net","errorBeacon":"bam.nr-data.net","licenseKey":"f46052bf0f","applicationID":"3606589","transactionName":"c1lfF0sNXlRRFhxBBFFVWQZLER1LXAtE","queueTime":0,"applicationTime":146,"agentToken":null,"agent":""}
  </script>
  <script type="text/javascript">
   (window.NREUM||(NREUM={})).loader_config={xpid:"VwEAU1VbGwAGVFdXDwg="};window.NREUM||(NREUM={}),__nr_require=function(t,e,n){function r(n){if(!e[n]){var o=e[n]={exports:{}};t[n][0].call(o.exports,function(e){var o=t[n][1][e];return r(o||e)},o,o.exports)}return e[n].exports}if("function"==typeof __nr_require)return __nr_require;for(var o=0;o<n.length;o++)r(n[o]);return r}({1:[function(t,e,n){function r(t){try{c.console&&console.log(t)}catch(e){}}var o,i=t("ee"),a=t(12),c={};try{o=localStorage.getItem("__nr_flags").split(","),console&&"function"==typeof console.log&&(c.console=!0,o.indexOf("dev")!==-1&&(c.dev=!0),o.indexOf("nr_dev")!==-1&&(c.nrDev=!0))}catch(s){}c.nrDev&&i.on("internal-error",function(t){r(t.stack)}),c.dev&&i.on("fn-err",function(t,e,n){r(n.stack)}),c.dev&&(r("NR AGENT IN DEVELOPMENT MODE"),r("flags: "+a(c,function(t,e){return t}).join(", ")))},{}],2:[function(t,e,n){function r(t,e,n,r,c){try{p?p-=1:o(c||new UncaughtException(t,e,n),!0)}catch(f){try{i("ierr",[f,s.now(),!0])}catch(d){}}return"function"==typeof u&&u.apply(this,a(arguments))}function UncaughtException(t,e,n){this.message=t||"Uncaught error with no additional information",this.sourceURL=e,this.line=n}function o(t,e){var n=e?null:s.now();i("err",[t,n])}var i=t("handle"),a=t(13),c=t("ee"),s=t("loader"),f=t("gos"),u=window.onerror,d=!1,l="nr@seenError",p=0;s.features.err=!0,t(1),window.onerror=r;try{throw new Error}catch(h){"stack"in h&&(t(5),t(4),"addEventListener"in window&&t(3),s.xhrWrappable&&t(6),d=!0)}c.on("fn-start",function(t,e,n){d&&(p+=1)}),c.on("fn-err",function(t,e,n){d&&!n[l]&&(f(n,l,function(){return!0}),this.thrown=!0,o(n))}),c.on("fn-end",function(){d&&!this.thrown&&p>0&&(p-=1)}),c.on("internal-error",function(t){i("ierr",[t,s.now(),!0])})},{}],3:[function(t,e,n){function r(t){for(var e=t;e&&!e.hasOwnProperty(u);)e=Object.getPrototypeOf(e);e&&o(e)}function o(t){c.inPlace(t,[u,d],"-",i)}function i(t,e){return t[1]}var a=t("ee").get("events"),c=t(15)(a,!0),s=t("gos"),f=XMLHttpRequest,u="addEventListener",d="removeEventListener";e.exports=a,"getPrototypeOf"in Object?(r(document),r(window),r(f.prototype)):f.prototype.hasOwnProperty(u)&&(o(window),o(f.prototype)),a.on(u+"-start",function(t,e){var n=t[1],r=s(n,"nr@wrapped",function(){function t(){if("function"==typeof n.handleEvent)return n.handleEvent.apply(n,arguments)}var e={object:t,"function":n}[typeof n];return e?c(e,"fn-",null,e.name||"anonymous"):n});this.wrapped=t[1]=r}),a.on(d+"-start",function(t){t[1]=this.wrapped||t[1]})},{}],4:[function(t,e,n){var r=t("ee").get("raf"),o=t(15)(r),i="equestAnimationFrame";e.exports=r,o.inPlace(window,["r"+i,"mozR"+i,"webkitR"+i,"msR"+i],"raf-"),r.on("raf-start",function(t){t[0]=o(t[0],"fn-")})},{}],5:[function(t,e,n){function r(t,e,n){t[0]=a(t[0],"fn-",null,n)}function o(t,e,n){this.method=n,this.timerDuration=isNaN(t[1])?0:+t[1],t[0]=a(t[0],"fn-",this,n)}var i=t("ee").get("timer"),a=t(15)(i),c="setTimeout",s="setInterval",f="clearTimeout",u="-start",d="-";e.exports=i,a.inPlace(window,[c,"setImmediate"],c+d),a.inPlace(window,[s],s+d),a.inPlace(window,[f,"clearImmediate"],f+d),i.on(s+u,r),i.on(c+u,o)},{}],6:[function(t,e,n){function r(t,e){d.inPlace(e,["onreadystatechange"],"fn-",c)}function o(){var t=this,e=u.context(t);t.readyState>3&&!e.resolved&&(e.resolved=!0,u.emit("xhr-resolved",[],t)),d.inPlace(t,w,"fn-",c)}function i(t){g.push(t),h&&(b?b.then(a):v?v(a):(E=-E,O.data=E))}function a(){for(var t=0;t<g.length;t++)r([],g[t]);g.length&&(g=[])}function c(t,e){return e}function s(t,e){for(var n in t)e[n]=t[n];return e}t(3);var f=t("ee"),u=f.get("xhr"),d=t(15)(u),l=NREUM.o,p=l.XHR,h=l.MO,m=l.PR,v=l.SI,y="readystatechange",w=["onload","onerror","onabort","onloadstart","onloadend","onprogress","ontimeout"],g=[];e.exports=u;var x=window.XMLHttpRequest=function(t){var e=new p(t);try{u.emit("new-xhr",[e],e),e.addEventListener(y,o,!1)}catch(n){try{u.emit("internal-error",[n])}catch(r){}}return e};if(s(p,x),x.prototype=p.prototype,d.inPlace(x.prototype,["open","send"],"-xhr-",c),u.on("send-xhr-start",function(t,e){r(t,e),i(e)}),u.on("open-xhr-start",r),h){var b=m&&m.resolve();if(!v&&!m){var E=1,O=document.createTextNode(E);new h(a).observe(O,{characterData:!0})}}else f.on("fn-end",function(t){t[0]&&t[0].type===y||a()})},{}],7:[function(t,e,n){function r(t){var e=this.params,n=this.metrics;if(!this.ended){this.ended=!0;for(var r=0;r<d;r++)t.removeEventListener(u[r],this.listener,!1);if(!e.aborted){if(n.duration=a.now()-this.startTime,4===t.readyState){e.status=t.status;var i=o(t,this.lastSize);if(i&&(n.rxSize=i),this.sameOrigin){var s=t.getResponseHeader("X-NewRelic-App-Data");s&&(e.cat=s.split(", ").pop())}}else e.status=0;n.cbTime=this.cbTime,f.emit("xhr-done",[t],t),c("xhr",[e,n,this.startTime])}}}function o(t,e){var n=t.responseType;if("json"===n&&null!==e)return e;var r="arraybuffer"===n||"blob"===n||"json"===n?t.response:t.responseText;return h(r)}function i(t,e){var n=s(e),r=t.params;r.host=n.hostname+":"+n.port,r.pathname=n.pathname,t.sameOrigin=n.sameOrigin}var a=t("loader");if(a.xhrWrappable){var c=t("handle"),s=t(8),f=t("ee"),u=["load","error","abort","timeout"],d=u.length,l=t("id"),p=t(11),h=t(10),m=window.XMLHttpRequest;a.features.xhr=!0,t(6),f.on("new-xhr",function(t){var e=this;e.totalCbs=0,e.called=0,e.cbTime=0,e.end=r,e.ended=!1,e.xhrGuids={},e.lastSize=null,p&&(p>34||p<10)||window.opera||t.addEventListener("progress",function(t){e.lastSize=t.loaded},!1)}),f.on("open-xhr-start",function(t){this.params={method:t[0]},i(this,t[1]),this.metrics={}}),f.on("open-xhr-end",function(t,e){"loader_config"in NREUM&&"xpid"in NREUM.loader_config&&this.sameOrigin&&e.setRequestHeader("X-NewRelic-ID",NREUM.loader_config.xpid)}),f.on("send-xhr-start",function(t,e){var n=this.metrics,r=t[0],o=this;if(n&&r){var i=h(r);i&&(n.txSize=i)}this.startTime=a.now(),this.listener=function(t){try{"abort"===t.type&&(o.params.aborted=!0),("load"!==t.type||o.called===o.totalCbs&&(o.onloadCalled||"function"!=typeof e.onload))&&o.end(e)}catch(n){try{f.emit("internal-error",[n])}catch(r){}}};for(var c=0;c<d;c++)e.addEventListener(u[c],this.listener,!1)}),f.on("xhr-cb-time",function(t,e,n){this.cbTime+=t,e?this.onloadCalled=!0:this.called+=1,this.called!==this.totalCbs||!this.onloadCalled&&"function"==typeof n.onload||this.end(n)}),f.on("xhr-load-added",function(t,e){var n=""+l(t)+!!e;this.xhrGuids&&!this.xhrGuids[n]&&(this.xhrGuids[n]=!0,this.totalCbs+=1)}),f.on("xhr-load-removed",function(t,e){var n=""+l(t)+!!e;this.xhrGuids&&this.xhrGuids[n]&&(delete this.xhrGuids[n],this.totalCbs-=1)}),f.on("addEventListener-end",function(t,e){e instanceof m&&"load"===t[0]&&f.emit("xhr-load-added",[t[1],t[2]],e)}),f.on("removeEventListener-end",function(t,e){e instanceof m&&"load"===t[0]&&f.emit("xhr-load-removed",[t[1],t[2]],e)}),f.on("fn-start",function(t,e,n){e instanceof m&&("onload"===n&&(this.onload=!0),("load"===(t[0]&&t[0].type)||this.onload)&&(this.xhrCbStart=a.now()))}),f.on("fn-end",function(t,e){this.xhrCbStart&&f.emit("xhr-cb-time",[a.now()-this.xhrCbStart,this.onload,e],e)})}},{}],8:[function(t,e,n){e.exports=function(t){var e=document.createElement("a"),n=window.location,r={};e.href=t,r.port=e.port;var o=e.href.split("://");!r.port&&o[1]&&(r.port=o[1].split("/")[0].split("@").pop().split(":")[1]),r.port&&"0"!==r.port||(r.port="https"===o[0]?"443":"80"),r.hostname=e.hostname||n.hostname,r.pathname=e.pathname,r.protocol=o[0],"/"!==r.pathname.charAt(0)&&(r.pathname="/"+r.pathname);var i=!e.protocol||":"===e.protocol||e.protocol===n.protocol,a=e.hostname===document.domain&&e.port===n.port;return r.sameOrigin=i&&(!e.hostname||a),r}},{}],9:[function(t,e,n){function r(){}function o(t,e,n){return function(){return i(t,[f.now()].concat(c(arguments)),e?null:this,n),e?void 0:this}}var i=t("handle"),a=t(12),c=t(13),s=t("ee").get("tracer"),f=t("loader"),u=NREUM;"undefined"==typeof window.newrelic&&(newrelic=u);var d=["setPageViewName","setCustomAttribute","setErrorHandler","finished","addToTrace","inlineHit","addRelease"],l="api-",p=l+"ixn-";a(d,function(t,e){u[e]=o(l+e,!0,"api")}),u.addPageAction=o(l+"addPageAction",!0),u.setCurrentRouteName=o(l+"routeName",!0),e.exports=newrelic,u.interaction=function(){return(new r).get()};var h=r.prototype={createTracer:function(t,e){var n={},r=this,o="function"==typeof e;return i(p+"tracer",[f.now(),t,n],r),function(){if(s.emit((o?"":"no-")+"fn-start",[f.now(),r,o],n),o)try{return e.apply(this,arguments)}catch(t){throw s.emit("fn-err",[arguments,this,t],n),t}finally{s.emit("fn-end",[f.now()],n)}}}};a("setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","),function(t,e){h[e]=o(p+e)}),newrelic.noticeError=function(t){"string"==typeof t&&(t=new Error(t)),i("err",[t,f.now()])}},{}],10:[function(t,e,n){e.exports=function(t){if("string"==typeof t&&t.length)return t.length;if("object"==typeof t){if("undefined"!=typeof ArrayBuffer&&t instanceof ArrayBuffer&&t.byteLength)return t.byteLength;if("undefined"!=typeof Blob&&t instanceof Blob&&t.size)return t.size;if(!("undefined"!=typeof FormData&&t instanceof FormData))try{return JSON.stringify(t).length}catch(e){return}}}},{}],11:[function(t,e,n){var r=0,o=navigator.userAgent.match(/Firefox[\/\s](\d+\.\d+)/);o&&(r=+o[1]),e.exports=r},{}],12:[function(t,e,n){function r(t,e){var n=[],r="",i=0;for(r in t)o.call(t,r)&&(n[i]=e(r,t[r]),i+=1);return n}var o=Object.prototype.hasOwnProperty;e.exports=r},{}],13:[function(t,e,n){function r(t,e,n){e||(e=0),"undefined"==typeof n&&(n=t?t.length:0);for(var r=-1,o=n-e||0,i=Array(o<0?0:o);++r<o;)i[r]=t[e+r];return i}e.exports=r},{}],14:[function(t,e,n){e.exports={exists:"undefined"!=typeof window.performance&&window.performance.timing&&"undefined"!=typeof window.performance.timing.navigationStart}},{}],15:[function(t,e,n){function r(t){return!(t&&t instanceof Function&&t.apply&&!t[a])}var o=t("ee"),i=t(13),a="nr@original",c=Object.prototype.hasOwnProperty,s=!1;e.exports=function(t,e){function n(t,e,n,o){function nrWrapper(){var r,a,c,s;try{a=this,r=i(arguments),c="function"==typeof n?n(r,a):n||{}}catch(f){l([f,"",[r,a,o],c])}u(e+"start",[r,a,o],c);try{return s=t.apply(a,r)}catch(d){throw u(e+"err",[r,a,d],c),d}finally{u(e+"end",[r,a,s],c)}}return r(t)?t:(e||(e=""),nrWrapper[a]=t,d(t,nrWrapper),nrWrapper)}function f(t,e,o,i){o||(o="");var a,c,s,f="-"===o.charAt(0);for(s=0;s<e.length;s++)c=e[s],a=t[c],r(a)||(t[c]=n(a,f?c+o:o,i,c))}function u(n,r,o){if(!s||e){var i=s;s=!0;try{t.emit(n,r,o,e)}catch(a){l([a,n,r,o])}s=i}}function d(t,e){if(Object.defineProperty&&Object.keys)try{var n=Object.keys(t);return n.forEach(function(n){Object.defineProperty(e,n,{get:function(){return t[n]},set:function(e){return t[n]=e,e}})}),e}catch(r){l([r])}for(var o in t)c.call(t,o)&&(e[o]=t[o]);return e}function l(e){try{t.emit("internal-error",e)}catch(n){}}return t||(t=o),n.inPlace=f,n.flag=a,n}},{}],ee:[function(t,e,n){function r(){}function o(t){function e(t){return t&&t instanceof r?t:t?s(t,c,i):i()}function n(n,r,o,i){if(!l.aborted||i){t&&t(n,r,o);for(var a=e(o),c=h(n),s=c.length,f=0;f<s;f++)c[f].apply(a,r);var d=u[w[n]];return d&&d.push([g,n,r,a]),a}}function p(t,e){y[t]=h(t).concat(e)}function h(t){return y[t]||[]}function m(t){return d[t]=d[t]||o(n)}function v(t,e){f(t,function(t,n){e=e||"feature",w[n]=e,e in u||(u[e]=[])})}var y={},w={},g={on:p,emit:n,get:m,listeners:h,context:e,buffer:v,abort:a,aborted:!1};return g}function i(){return new r}function a(){(u.api||u.feature)&&(l.aborted=!0,u=l.backlog={})}var c="nr@context",s=t("gos"),f=t(12),u={},d={},l=e.exports=o();l.backlog=u},{}],gos:[function(t,e,n){function r(t,e,n){if(o.call(t,e))return t[e];var r=n();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(t,e,{value:r,writable:!0,enumerable:!1}),r}catch(i){}return t[e]=r,r}var o=Object.prototype.hasOwnProperty;e.exports=r},{}],handle:[function(t,e,n){function r(t,e,n,r){o.buffer([t],r),o.emit(t,e,n)}var o=t("ee").get("handle");e.exports=r,r.ee=o},{}],id:[function(t,e,n){function r(t){var e=typeof t;return!t||"object"!==e&&"function"!==e?-1:t===window?0:a(t,i,function(){return o++})}var o=1,i="nr@id",a=t("gos");e.exports=r},{}],loader:[function(t,e,n){function r(){if(!b++){var t=x.info=NREUM.info,e=l.getElementsByTagName("script")[0];if(setTimeout(u.abort,3e4),!(t&&t.licenseKey&&t.applicationID&&e))return u.abort();f(w,function(e,n){t[e]||(t[e]=n)}),s("mark",["onload",a()+x.offset],null,"api");var n=l.createElement("script");n.src="https://"+t.agent,e.parentNode.insertBefore(n,e)}}function o(){"complete"===l.readyState&&i()}function i(){s("mark",["domContent",a()+x.offset],null,"api")}function a(){return E.exists&&performance.now?Math.round(performance.now()):(c=Math.max((new Date).getTime(),c))-x.offset}var c=(new Date).getTime(),s=t("handle"),f=t(12),u=t("ee"),d=window,l=d.document,p="addEventListener",h="attachEvent",m=d.XMLHttpRequest,v=m&&m.prototype;NREUM.o={ST:setTimeout,SI:d.setImmediate,CT:clearTimeout,XHR:m,REQ:d.Request,EV:d.Event,PR:d.Promise,MO:d.MutationObserver};var y=""+location,w={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",agent:"js-agent.newrelic.com/nr-1071.min.js"},g=m&&v&&v[p]&&!/CriOS/.test(navigator.userAgent),x=e.exports={offset:c,now:a,origin:y,features:{},xhrWrappable:g};t(9),l[p]?(l[p]("DOMContentLoaded",i,!1),d[p]("load",r,!1)):(l[h]("onreadystatechange",o),d[h]("onload",r)),s("mark",["firstbyte",c],null,"api");var b=0,E=t(14)},{}]},{},["loader",2,7]);
  </script>
  <meta content="width=device-width, initial-scale=1, minimum-scale=1.0, maximum-scale=1, user-scalable=no" name="viewport"/>
  <meta content="E797MgrWewAoj3f3d2qOtnwdjPZIXrkC0asUIbhlehw" name="google-site-verification"/>
  <meta content="David Towber is a visual arts teacher at Hunter College High School in New York, NY. Review David Towber's ratings by students and parents." name="description"/>
  <meta content="https://www.ratemyteachers.com/images/logo_icon_1000.png" property="twitter:image"/>
  <meta content="https://www.ratemyteachers.com/images/logo_icon_1000.png" property="og:image"/>
  <meta content="David Towber - Hunter College High School | RateMyTeachers" property="og:title"/>
  <meta content="profile" property="og:type"/>
  <meta content="https://www.ratemyteachers.com/david-towber/172358-t" property="og:url"/>
  <meta content="RateMyTeachers.com" property="og:site_name"/>
  <meta content="David Towber is a visual arts teacher at Hunter College High School in New York, NY. Review David Towber's ratings by students and parents." property="og:description"/>
  <meta content="unsafe-url" name="referrer"/>
  <meta content="noodp,noydir" name="robots"/>
  <meta content="https://www.ratemyteachers.com/apple_touch_icon_196x196.png" property="rmt:image"/>
  <link href="/favicon.ico" rel="shortcut icon" sizes="64x64 48x48 32x32 16x16" type="image/x-icon"/>
  <link href="/apple_touch_icon_60x60.png" rel="apple-touch-icon"/>
  <link href="/apple_touch_icon_76x76.png" rel="apple-touch-icon" sizes="76x76"/>
  <link href="/apple_touch_icon_120x120.png" rel="apple-touch-icon" sizes="120x120"/>
  <link href="/apple_touch_icon_152x152.png" rel="apple-touch-icon" sizes="152x152"/>
  <link href="/apple_touch_icon_196x196.png" rel="apple-touch-icon-precomposed"/>
  <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"/>
  <link href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css" media="screen" rel="stylesheet"/>
  <link href="/assets/application-14a53ad0bb9a1fbc95784107ee093856.css" media="all" rel="stylesheet"/>
  <link href="https://code.jquery.com/ui/1.11.2/themes/smoothness/jquery-ui.css" rel="stylesheet"/>
  <script type="text/javascript">
   var currentState = 'NY';

  var siteConfig = {
    homepage_reload_tab: false,
    enableAnalytics:     true,
    debugMode:           false,
    asyncScripts:        true
  };


  function getWindowWidth() {
    var myWidth = 0, myHeight = 0;
    if( typeof( window.innerWidth ) === 'number' ) {
      myWidth = window.innerWidth; myHeight = window.innerHeight;
    } else if( document.documentElement && ( document.documentElement.clientWidth ||document.documentElement.clientHeight ) ) {
      myWidth = document.documentElement.clientWidth; myHeight = document.documentElement.clientHeight;
    } else if( document.body && ( document.body.clientWidth || document.body.clientHeight ) ) {
      myWidth = document.body.clientWidth; myHeight = document.body.clientHeight;
    }
    return myWidth;
  }

  var isDesktopVariant = true;
  var isTabletVariant = false;
  var isMobileVariant = false;
  var isExtraSmall = (getWindowWidth() < 768) || (screen ? screen.width < 768 : false);
  var isMobile = isExtraSmall || isMobileVariant;
  var isMedium = (getWindowWidth() < 1200) || (screen ? screen.width < 1200 : false);


  var isChrome = navigator.userAgent.indexOf('Chrome') > -1;
  var isExplorer = navigator.userAgent.indexOf('MSIE') > -1;
  var isFirefox = navigator.userAgent.indexOf('Firefox') > -1;
  var isSafari = navigator.userAgent.indexOf("Safari") > -1;
  var isOpera = navigator.userAgent.toLowerCase().indexOf("op") > -1;
  if ((isChrome)&&(isSafari)) {isSafari=false;}
  if ((isChrome)&&(isOpera)) {isChrome=false;}

  var enablePropel    = !isSafari && !isOpera && false;
  var enableMediabong = !isSafari && !isOpera;
  var enableBrightComedia = !isSafari && !isOpera;

  var isMobileUpload = false;

    var cseData = {
      isCseSearch: true
      ,paramFormat: '%{search_term}%{location}'
      ,stateList: [{"name":"Alaska","shortname":"ak"},{"name":"Alabama","shortname":"al"},{"name":"Arkansas","shortname":"ar"},{"name":"Arizona","shortname":"az"},{"name":"California","shortname":"ca"},{"name":"Colorado","shortname":"co"},{"name":"Connecticut","shortname":"ct"},{"name":"Dc","shortname":"dc"},{"name":"Delaware","shortname":"de"},{"name":"Florida","shortname":"fl"},{"name":"Georgia","shortname":"ga"},{"name":"Hawaii","shortname":"hi"},{"name":"Iowa","shortname":"ia"},{"name":"Idaho","shortname":"id"},{"name":"Illinois","shortname":"il"},{"name":"Indiana","shortname":"in"},{"name":"Kansas","shortname":"ks"},{"name":"Kentucky","shortname":"ky"},{"name":"Louisiana","shortname":"la"},{"name":"Massachusetts","shortname":"ma"},{"name":"Maryland","shortname":"md"},{"name":"Maine","shortname":"me"},{"name":"Michigan","shortname":"mi"},{"name":"Minnesota","shortname":"mn"},{"name":"Missouri","shortname":"mo"},{"name":"Mississippi","shortname":"ms"},{"name":"Montana","shortname":"mt"},{"name":"North Carolina","shortname":"nc"},{"name":"North Dakota","shortname":"nd"},{"name":"Nebraska","shortname":"ne"},{"name":"New Hampshire","shortname":"nh"},{"name":"New Jersey","shortname":"nj"},{"name":"New Mexico","shortname":"nm"},{"name":"Nevada","shortname":"nv"},{"name":"New York","shortname":"ny"},{"name":"Ohio","shortname":"oh"},{"name":"Oklahoma","shortname":"ok"},{"name":"Oregon","shortname":"or"},{"name":"Pennsylvania","shortname":"pa"},{"name":"Puerto Rico","shortname":"pr"},{"name":"Rhode Island","shortname":"ri"},{"name":"South Carolina","shortname":"sc"},{"name":"South Dakota","shortname":"sd"},{"name":"Tennessee","shortname":"tn"},{"name":"Texas","shortname":"tx"},{"name":"Utah","shortname":"ut"},{"name":"Virginia","shortname":"va"},{"name":"Vermont","shortname":"vt"},{"name":"Washington","shortname":"wa"},{"name":"Wisconsin","shortname":"wi"},{"name":"West Virginia","shortname":"wv"},{"name":"Wyoming","shortname":"wy"}]
    };


  // Search autocomplete widget
  var searchAutocompleteHTML = "<div class=\'desktop search_autocomplete_widget\'>\n<div class=\'autocomplete_teachers\'>\n<div class=\'autocomplete_subtitle\'>\n<i class=\'fa fa-user\'><\/i>\nTeachers and Professors\n<\/div>\n<div class=\'autocomplete_container\'>\n<div class=\'amp_ads_autocomplete_widget\' id=\'amp_ads_autocomplete\'><\/div>\n<div class=\'autocomplete_elements_container\'>\n<a class=\'autocomplete_element\' target=\'_blank\'>\n<span class=\'autocomplete_name\'><\/span>\n<span class=\'autocomplete_school_name\'><\/span>\n<\/a>\n<\/div>\n<\/div>\n<a class=\'autocomplete_view_more\'>\nView All\n<span class=\'autocomplete_count\'><\/span>\nTeachers and Professors\n<i class=\'fa fa-chevron-right\'><\/i>\n<\/a>\n<\/div>\n<div class=\'autocomplete_schools\'>\n<div class=\'autocomplete_subtitle\'>\n<i class=\'fa fa-university\'><\/i>\nSchools and Colleges\n<\/div>\n<div class=\'autocomplete_container\'>\n<div class=\'autocomplete_elements_container\'>\n<a class=\'autocomplete_element\' target=\'_blank\'>\n<span class=\'autocomplete_name\'><\/span>\n<span class=\'autocomplete_address\'><\/span>\n<\/a>\n<\/div>\n<\/div>\n<a class=\'autocomplete_view_more\'>\nView All\n<span class=\'autocomplete_count\'><\/span>\nSchools and Colleges\n<i class=\'fa fa-chevron-right\'><\/i>\n<\/a>\n<\/div>\n<\/div>\n";
  </script>
  <script type="text/javascript">
   // Async functions variable
  functionToLoad = [];
  
  // Fastest way to check if an object is an array
  functionToLoad.isArrayObj = function(obj) {
    return !!obj && obj.constructor === Array;
  };
  
  // Extract data from an element
  functionToLoad.extractElementData = function(elementData) {
    var data = {
      element: elementData
      ,async: false
      ,subElements: []
    };
    
    // The element is an array, check for async option
    if (this.isArrayObj(elementData) && elementData.length > 0) {
      data.async = !!elementData[1];
      data.element = elementData[0];
      data.subElements = elementData[2] || [];
    }
    return data;
  };
  
  // Wrap push functionality
  functionToLoad.realPush = functionToLoad.push;
  functionToLoad.executePush = function(args) {
    var data = this.extractElementData(args);

    // Inject script tag on inplace
    if (typeof data.element === 'string') {
      // Inject external file
      document.write('<script type="text/javascript" src="' + data.element + '"><\/script>');
    } else {
      // Inject function
      document.write('<script type="text/javascript">(');
      document.write(data.element.toString());
      document.write(')();<\/script>');
    }
    
    // Execute child scripts
    if (data.subElements.length > 0) {
      this.executePush(data.subElements);
    }
  };
  functionToLoad.push = function(args) {
    if (siteConfig.asyncScripts) {
      if (siteConfig.debugMode) { console.log('Async Script'); }
      
      // Async scripts so add it to array for later execution
      this.realPush(args);
      return;
    }
    if (siteConfig.debugMode) { console.log('Sync Script'); }
    
    // No async scripts, execute it right away
    this.executePush(args);
  };
  </script>
  <script type="text/javascript">
   _googlePush = function(a) {};
  </script>
  <script type="text/javascript">
   functionToLoad.push('//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js');
  functionToLoad.push('//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js');
  </script>
  <script>
   functionToLoad.push(function() {
        gaId = 'UA-4216499-1';

        (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
        (i[r].q=i[r].q||[]).push(arguments);},i[r].l=1*new Date();a=s.createElement(o),
        m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m);
        })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
        ga('create', gaId, 'auto');
        ga('require', 'displayfeatures');
        //ga('require', 'ecommerce', 'ecommerce.js');
      });
  </script>
  <script type="text/javascript">
   functionToLoad.push('/assets/rmt.analytics-b3702f400256546899eddf8b81076656.js');
  </script>
  <script>
   functionToLoad.push(function(){
    pageType = "";
    RMT.Analytics.trackPageview({dimensions: [{key: 'dimension1', value: pageType}]});
    searchTerm = "";
  });
  </script>
  <script type="text/javascript">
   // Returns a function, that, as long as it continues to be invoked, will not
    // be triggered. The function will be called after it stops being called for
    // N milliseconds. If `immediate` is passed, trigger the function on the
    // leading edge, instead of the trailing.
    function debounce(func, wait, immediate) {
      var timeout;
      return function() {
        var context = this, args = arguments;
        var later = function() {
          timeout = null;
          if (!immediate) func.apply(context, args);
        };
        var callNow = immediate && !timeout;
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
        if (callNow) func.apply(context, args);
      };
    };
  </script>
  <script data-cfasync="false" type="text/javascript">
   functionToLoad.push([function() {
    window.apd_options = { 'websiteId': 6292, 'runFromFrame': false };
    (function() {
      var w = window.apd_options.runFromFrame ? window.top : window;
      if(window.apd_options.runFromFrame && w!=window.parent) w=window.parent;
      if (w.location.hash.indexOf('apdAdmin') != -1){if(typeof(Storage) !== 'undefined') {w.localStorage.apdAdmin = 1;}}
      var adminMode = ((typeof(Storage) == 'undefined') || (w.localStorage.apdAdmin == 1));
      w.apd_options=window.apd_options;
      var apd = w.document.createElement('script'); apd.type = 'text/javascript'; apd.async = true;
      apd.src = '//' + (adminMode ? 'cdn' : 'ecdn') + '.firstimpression.io/' + (adminMode ? 'fi.js?id=' + window.apd_options.websiteId : 'fi_client.js') ;
      var s = w.document.getElementsByTagName('head')[0]; s.appendChild(apd);
    })();
  }, true]);
  </script>
  <script charset="utf-8" type="text/javascript">
   functionToLoad.push(function() {
        (function(G,o,O,g,L,e){G[g]=G[g]||function(){(G[g]['q']=G[g]['q']||[]).push(
        arguments)},G[g]['t']=1*new Date;L=o.createElement(O),e=o.getElementsByTagName(
        O)[0];L.async=1;L.src='//www.google.com/adsense/search/async-ads.js';
        e.parentNode.insertBefore(L,e)})(window,document,'script','_googCsa');
      });
  </script>
  <script type="text/javascript">
   functionToLoad.push('//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js');
  </script>
  <script type="text/javascript">
   functionToLoad.push(function() {
        window.deployads=[];
        window.deployads.push=function(){
          var b=document.querySelectorAll('script[type\x3d"text/x-ab-test"]:not([data-processed])');
          if(b&&0<b.length){
            var b=b[0];
            var a=b.innerHTML.replace(/xscript/g,"script");
            document.write(a);
            b.setAttribute("data-processed","true");
          }
        }
      });
  </script>
  <script type="text/javascript">
   functionToLoad.push(function() {

      var LazyAds = function(){
        // this.elements = {};
      };


      LazyAds.init = function(delay){
        this.elements = {};
        var self = this;
        if (typeof(delay) === 'undefined' || delay === null)
          delay = 10000;
        else
          console.info('Set LazyAds delay to ' + delay + 'ms');


        $(window).load(function() {
          // self.domLoaded = true;
          // console.log('LazyAds: window load');
          setTimeout(function() {
            self.domLoaded = true;
            self.refresh();
          }, delay);
          // self.refresh();
        });

        var scrollHandler = debounce(function(e){
          self.refresh();
        }, 100);
        jQuery(document).scroll(scrollHandler);
      };

      /* id:  can ben ID of en element, or a scroll offset */
      LazyAds.register = function(id, callback, opts) {
        // console.log('LazyAds: register ' + id);
        this.elements[ id ] = { loaded: false, callback: callback };
        this.refresh();
      };


      LazyAds.refresh = function() {
        var el, isVisible;
        var scrollY = window.scrollY;
        // console.log("LazyAds: scrollY " + scrollY);
        for(var id in this.elements) {
          if (!this.elements.hasOwnProperty(id)) continue;
          if(this.elements[id].loaded) continue;

          isVisible = false || this.domLoaded;

          if (!isVisible) {
            // handle scroll position
            if (/^\d+$/.test(id)) {
              // console.log('id is an offset');
              if( scrollY >= id ) {
                isVisible = true;
              }
            } else if( this.isVisible(id) ) {
              isVisible = true;
            }
          }

          if (isVisible) {
            this.elements[id].loaded = true;
            console.info('LazyAds: execute callback for ' + id);
            this.elements[id].callback();
            delete this.elements[id];
          }



        }
      };


      LazyAds.isVisible = function(id) {
        // https://github.com/customd/jquery-visible/blob/master/jquery.visible.js
        var $t        = $('#' + id);

        // if the id doesn't exist just bounce.
        if( !$t[0] ) return false;

        var $w        = $(window),  // todo refactor this
            t         = $t.get(0),
            vpWidth   = $w.width(),
            vpHeight  = $w.height(),
            direction = (direction) ? direction : 'both',
            clientSize = t.offsetWidth * t.offsetHeight;
            // clientSize = hidden === true ? t.offsetWidth * t.offsetHeight : true;

        if (typeof t.getBoundingClientRect === 'function'){

            // Use this native browser method, if available.
            var rec = t.getBoundingClientRect(),
                tViz = rec.top    >= 0 && rec.top    <  vpHeight,
                bViz = rec.bottom >  0 && rec.bottom <= vpHeight,
                lViz = rec.left   >= 0 && rec.left   <  vpWidth,
                rViz = rec.right  >  0 && rec.right  <= vpWidth,
                vVisible   = tViz || bViz,
                hVisible   = lViz || rViz;

            if(direction === 'both')
                return clientSize && vVisible && hVisible;
            else if(direction === 'vertical')
                return clientSize && vVisible;
            else if(direction === 'horizontal')
                return clientSize && hVisible;
        } else {

            var viewTop         = $w.scrollTop(),
                viewBottom      = viewTop + vpHeight,
                viewLeft        = $w.scrollLeft(),
                viewRight       = viewLeft + vpWidth,
                offset          = $t.offset(),
                _top            = offset.top,
                _bottom         = _top + $t.height(),
                _left           = offset.left,
                _right          = _left + $t.width(),
                compareTop      = _bottom,
                compareBottom   = _top,
                compareLeft     = _right,
                compareRight    = _left;

            if(direction === 'both')
                return !!clientSize && ((compareBottom <= viewBottom) && (compareTop >= viewTop)) && ((compareRight <= viewRight) && (compareLeft >= viewLeft));
            else if(direction === 'vertical')
                return !!clientSize && ((compareBottom <= viewBottom) && (compareTop >= viewTop));
            else if(direction === 'horizontal')
                return !!clientSize && ((compareRight <= viewRight) && (compareLeft >= viewLeft));
        }
      };



      var delay = 6000;
      LazyAds.init(delay);

      // (function() {
      //   var delay = 6000;
      //   LazyAds.init();
      // })();
    });
  </script>
  <script type="text/javascript">
   var _session = {};
  </script>
  <script type="text/javascript">
   functionToLoad.push(["//tags-cdn.deployads.com/a/ratemyteachers.com.js", true,[
        function() {
          (deployads = window.deployads || []).push({});
        }
      ]]);
  </script>
  <link href="https://www.ratemyteachers.com/david-towber/172358-t.rss" rel="alternate" type="application/rss+xml"/>
  <meta content="authenticity_token" name="csrf-param"/>
  <meta content="RIse6wKiFCcq5YO758BqgTkf4k/OLsixUl31QW6gU6M=" name="csrf-token"/>
 </head>
 <body class="inner_page teacher_page teacher_page_v7_1 ">
  <div id="fb-root">
  </div>
  <div class="rate_my_teachers_international">
   <div class="container">
    <div class="row">
     <a alt="United States" class="country active" href="https://www.ratemyteachers.com" title="United States">
      United States
     </a>
     <a alt="Canada" class="country " href="https://ca.ratemyteachers.com" title="Canada">
      Canada
     </a>
     <a alt="United Kingdom" class="country " href="https://uk.ratemyteachers.com" title="United Kingdom">
      United Kingdom
     </a>
     <a alt="Australia" class="country " href="https://au.ratemyteachers.com" title="Australia">
      Australia
     </a>
     <a alt="New Zealand" class="country " href="https://nz.ratemyteachers.com" title="New Zealand">
      New Zealand
     </a>
     <a alt="Ireland" class="country " href="https://ie.ratemyteachers.com" title="Ireland">
      Ireland
     </a>
     <div class="pull-right user_top_nav">
     </div>
    </div>
   </div>
  </div>
  <header>
   <div class="container">
    <div class="row">
     <form action="/search_page" class="tab-form search_form trigger_to_main_search" method="get">
      <a alt="Go to RateMyTeachers Home" href="/" id="rate_my_teachers_logo" title="Go to RateMyTeachers Home">
      </a>
      <input name="search" type="hidden" value="teachers"/>
      <div class="search_inputs">
       <div class="bg">
        <div class="padding">
         <input class="search_input" name="q" placeholder="Search: School Name, City" type="text"/>
        </div>
        <div class="location">
         <select class="state" id="state" name="state">
          <option value="">
           Select a State
          </option>
          <option value="ak">
           Alaska - AK
          </option>
          <option value="al">
           Alabama - AL
          </option>
          <option value="ar">
           Arkansas - AR
          </option>
          <option value="az">
           Arizona - AZ
          </option>
          <option value="ca">
           California - CA
          </option>
          <option value="co">
           Colorado - CO
          </option>
          <option value="ct">
           Connecticut - CT
          </option>
          <option value="dc">
           Dc - DC
          </option>
          <option value="de">
           Delaware - DE
          </option>
          <option value="fl">
           Florida - FL
          </option>
          <option value="ga">
           Georgia - GA
          </option>
          <option value="hi">
           Hawaii - HI
          </option>
          <option value="ia">
           Iowa - IA
          </option>
          <option value="id">
           Idaho - ID
          </option>
          <option value="il">
           Illinois - IL
          </option>
          <option value="in">
           Indiana - IN
          </option>
          <option value="ks">
           Kansas - KS
          </option>
          <option value="ky">
           Kentucky - KY
          </option>
          <option value="la">
           Louisiana - LA
          </option>
          <option value="ma">
           Massachusetts - MA
          </option>
          <option value="md">
           Maryland - MD
          </option>
          <option value="me">
           Maine - ME
          </option>
          <option value="mi">
           Michigan - MI
          </option>
          <option value="mn">
           Minnesota - MN
          </option>
          <option value="mo">
           Missouri - MO
          </option>
          <option value="ms">
           Mississippi - MS
          </option>
          <option value="mt">
           Montana - MT
          </option>
          <option value="nc">
           North Carolina - NC
          </option>
          <option value="nd">
           North Dakota - ND
          </option>
          <option value="ne">
           Nebraska - NE
          </option>
          <option value="nh">
           New Hampshire - NH
          </option>
          <option value="nj">
           New Jersey - NJ
          </option>
          <option value="nm">
           New Mexico - NM
          </option>
          <option value="nv">
           Nevada - NV
          </option>
          <option value="ny">
           New York - NY
          </option>
          <option value="oh">
           Ohio - OH
          </option>
          <option value="ok">
           Oklahoma - OK
          </option>
          <option value="or">
           Oregon - OR
          </option>
          <option value="pa">
           Pennsylvania - PA
          </option>
          <option value="pr">
           Puerto Rico - PR
          </option>
          <option value="ri">
           Rhode Island - RI
          </option>
          <option value="sc">
           South Carolina - SC
          </option>
          <option value="sd">
           South Dakota - SD
          </option>
          <option value="tn">
           Tennessee - TN
          </option>
          <option value="tx">
           Texas - TX
          </option>
          <option value="ut">
           Utah - UT
          </option>
          <option value="va">
           Virginia - VA
          </option>
          <option value="vt">
           Vermont - VT
          </option>
          <option value="wa">
           Washington - WA
          </option>
          <option value="wi">
           Wisconsin - WI
          </option>
          <option value="wv">
           West Virginia - WV
          </option>
          <option value="wy">
           Wyoming - WY
          </option>
         </select>
        </div>
       </div>
       <div class="search_button">
        <button class="btn-search fa fa-search fa-3x" title="Search RateMyTeachers" type="submit">
        </button>
       </div>
      </div>
     </form>
    </div>
   </div>
  </header>
  <div class="container-fluid main-content">
   <div class="row">
    <section class="breadcrumbs container-fluid">
     <div class="row">
      <div class="container">
       <div class="col-sm-12">
        <ul class="list-inline collapsible_nav collapsible_nav_collapsed">
         <li class="toggle">
          <a href="javascript:void(0);" rel="nofollow">
           <i class="fa fa-bars">
           </i>
          </a>
         </li>
         <li class="collapse">
          <a href="/" title="Go to RateMyTeachers Home">
           United States
          </a>
         </li>
         <li class="collapse">
          <a alt="Go to Schools in New York" href="/new-york" title="Go to Schools in New York">
           New York
          </a>
         </li>
         <li class="collapse">
          <a alt="Go to Schools in New York" href="/new-york/new-york" title="Go to Schools in New York">
           New York
          </a>
         </li>
         <li class="always_show">
          <a alt="View Hunter College High School's Teachers" href="/hunter-college-high-school/25767-s" title="View Hunter College High School's Teachers">
           Hunter College High School
          </a>
         </li>
         <li class="collapse">
          <a href="/hunter-college-high-school/25767-s/visual-arts" title="View Visual Arts Teachers at Hunter College High School">
           Visual Arts
          </a>
         </li>
         <li class="collapse last">
          <span>
           David Towber
          </span>
         </li>
         <li class="always_show hidden-sm hidden-md hidden-lg extra_option">
          <a class="new_rating_trigger" data-backdrop="static" data-keyboard="" data-remote="/ratings/new?tid=172358" data-sender-name="Teacher page Breadcrum" data-target="#modal_rating" data-teacher="David Towber" data-toggle="modal" href="javascript:void(0);" rel="nofollow" remote="" title="Submit Rating for David Towber">
           Rate
David Towber
          </a>
         </li>
        </ul>
       </div>
      </div>
     </div>
    </section>
    <div class="container flash_container">
     <div class="row">
      <div class="col-xs-12">
       <div class="alert alert-danger" id="flash-error" style="display: none">
        <button class="close" data-dismiss="close" type="button">
         ×
        </button>
        <span>
        </span>
       </div>
       <div class="alert alert-warning" id="flash-alert" style="display: none">
        <button class="close" data-dismiss="close" type="button">
         ×
        </button>
        <span>
        </span>
       </div>
       <div class="alert alert-success" id="flash-success" style="display: none">
        <button class="close" data-dismiss="close" type="button">
         ×
        </button>
        <span>
        </span>
       </div>
       <div class="alert alert-info" id="flash-notice" style="display: none">
        <button class="close" data-dismiss="close" type="button">
         ×
        </button>
        <span>
        </span>
       </div>
      </div>
     </div>
    </div>
    <div id="content">
     <div class="container" itemscope="" itemtype="https://schema.org/ProfilePage">
      <meta content="2018-03-03" itemprop="dateModified"/>
      <div class="row">
       <section class="col-md-12 content">
        <div class="row">
         <div class="col-xs-9 primary_column">
          <div class="row teacher_info">
           <div class="col-xs-12 main_info">
            <div class="title_container" itemprop="about" itemscope="" itemtype="https://schema.org/Person">
             <h1 class="teacher_name">
              <meta content="David Towber" itemprop="name"/>
              <span>
               David Towber
              </span>
             </h1>
             <div class="extra">
              <h2 title="Hunter College High School">
               <a class="hidden-xs" href="/hunter-college-high-school/25767-s" title="Hunter College High School">
                <span itemprop="worksFor" itemscope="" itemtype="https://schema.org/School">
                 <span itemprop="name">
                  Hunter College High School
                 </span>
                </span>
               </a>
              </h2>
              <meta content="Visual Arts" itemprop="jobTitle"/>
              <a class="edit flag_teacher_trigger" data-backdrop="static" data-keyboard="" data-remote="/teachers/172358/flag" data-sender-name="Teacher page Main" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:void(0);" rel="nofollow" remote="" title="Submit a Correction">
               Flag
              </a>
             </div>
             <div class="teacher_actions" data-name="David Towber" data-sid="25767" data-status="-2" data-tid="172358" style="display:none; display: inline-block">
             </div>
            </div>
            <div class="details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="4.2 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 91.960px;">
                </div>
               </div>
              </div>
              <span class="rating-summary">
               Average
4.18
based on
53
teacher
ratings
              </span>
             </div>
             <div class="description">
              <strong>
               David Towber
              </strong>
              is
a
Visual Arts teacher
at
Hunter College High School
located in New York, New York.
When comparing David Towber's ratings to other
teachers in the state of
New York, David Towber's ratings are
below
the average of
4.39
stars.
Additionally, the average teacher rating at
Hunter College High School is 3.97
stars.
             </div>
            </div>
            <div class="col-xs-12">
             <div class="ad_container ATF_large">
              <div id="Teacher_ATF_Large_Leaderboard" style="text-align: center;">
               <div class="ad-tag" data-ad-name="lead_desktop_teach" data-ad-size="728x90">
               </div>
              </div>
             </div>
            </div>
            <div class="col-xs-12 attributes">
             <div class="attribute">
              <div class="easy val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
             <div class="attribute">
              <div class="knowledgeable val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Knowledge
              </div>
             </div>
             <div class="attribute">
              <div class="textbook_use val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Textbook Use
              </div>
             </div>
             <div class="attribute">
              <div class="exam_difficulty val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Exam Difficulty
              </div>
             </div>
            </div>
            <div class="footer">
             <div class="dn" itemprop="aggregateRating" itemscope="" itemtype="https://schema.org/AggregateRating">
              <meta content="53" itemprop="ratingCount"/>
              <meta content="53" itemprop="reviewCount"/>
              <meta content="4.18" itemprop="ratingValue"/>
              <meta content="5" itemprop="bestRating"/>
              <meta content="0" itemprop="worstRating"/>
             </div>
            </div>
           </div>
          </div>
          <div class="subheader">
           <div class="sticky_container_center">
            <div class="sticky_column">
             <div class="main_options">
              <a class="row school_name" href="/hunter-college-high-school/25767-s" title="View Hunter College High School's Teachers">
               <i class="fa fa-university">
               </i>
               <span>
                Hunter College High School
               </span>
              </a>
              <div class="row extra">
               <h3>
                <a class="col-xs-6 new_admin_request_trigger apply_admin" data-remote="/admin/new?sid=25767" data-school="Hunter College High School" data-sender="School page Mobile Search Form" data-target="#modal" data-toggle="modal" href="javascript:void(0);" rel="nofollow" title="Become Hunter College High School's Moderator">
                 <i class="fa fa-user-plus">
                 </i>
                 <span>
                  Become a Moderator!
                 </span>
                </a>
               </h3>
               <h3>
                <a class="col-xs-6 new_rating_trigger add_rating" data-backdrop="static" data-keyboard="" data-remote="/ratings/new?tid=172358" data-sender-name="Teacher page Main" data-target="#modal_rating" data-teacher="David Towber" data-toggle="modal" href="javascript:void(0);" rel="nofollow" remote="" title="Submit Rating for David Towber">
                 <i class="fa fa-star">
                 </i>
                 <span>
                  Add Rating
                 </span>
                </a>
               </h3>
              </div>
             </div>
            </div>
           </div>
          </div>
          <div class="row teacher_reviews">
           <div class="ad_container AMP">
            <div id="amp_ads_bottom">
            </div>
           </div>
           <div class="col-xs-12 no_toggle review secondary" id="rating_27007491" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r27007491">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="recommend val5 value">
               <i class="fa fa-check">
               </i>
               <span>
                5
               </span>
              </div>
              <div class="text">
               Recommended
              </div>
             </div>
             <div class="attribute">
              <div class="easy val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
             <div class="attribute">
              <div class="knowledgeable val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Knowledge
              </div>
             </div>
             <div class="attribute">
              <div class="textbook_use val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Textbook Use
              </div>
             </div>
             <div class="attribute">
              <div class="exam_difficulty val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Exam Difficulty
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="5.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 110.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="5.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2018-03-03" itemprop="datePublished">
               Mar 03, 2018
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               Mr. Towber is hilarious and amazing, he was very friendly and supportive. (I had him in 7th grade)
               <br/>
               <div class="submitted_by">
                <span class="hidden-xs">
                 Submitted by a student
                </span>
               </div>
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="27007491" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="27007491" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/27007491/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="27007491" style="display: none;">
             </div>
            </div>
           </div>
           <div class="ad_container taboola_video">
           </div>
           <div class="col-xs-12 no_toggle review" id="rating_26757873" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r26757873">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="recommend val5 value">
               <i class="fa fa-check">
               </i>
               <span>
                5
               </span>
              </div>
              <div class="text">
               Recommended
              </div>
             </div>
             <div class="attribute">
              <div class="easy val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
             <div class="attribute">
              <div class="knowledgeable val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Knowledge
              </div>
             </div>
             <div class="attribute">
              <div class="textbook_use val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Textbook Use
              </div>
             </div>
             <div class="attribute">
              <div class="exam_difficulty val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Exam Difficulty
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="5.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 110.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="5.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2017-12-15" itemprop="datePublished">
               Dec 15, 2017
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               I LOOOOOOVE MR TOWBER BEST TEACHER EVER =)
               <br/>
               <div class="submitted_by">
                <span class="hidden-xs">
                 Submitted by a student
                </span>
               </div>
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="26757873" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="26757873" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/26757873/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="26757873" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review secondary" id="rating_26509037" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r26509037">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="recommend val5 value">
               <i class="fa fa-check">
               </i>
               <span>
                5
               </span>
              </div>
              <div class="text">
               Recommended
              </div>
             </div>
             <div class="attribute">
              <div class="easy val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
             <div class="attribute">
              <div class="knowledgeable val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Knowledge
              </div>
             </div>
             <div class="attribute">
              <div class="textbook_use val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Textbook Use
              </div>
             </div>
             <div class="attribute">
              <div class="exam_difficulty val1 value">
               <span>
                1
               </span>
              </div>
              <div class="text">
               Exam Difficulty
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="5.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 110.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="5.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2017-10-02" itemprop="datePublished">
               Oct 02, 2017
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               Mr. Towber is truly really nice man. I had the pleasure of having him in 9th grade and I took Art History. He has a great sense of humor and is very forgiving and lovely. Just don't mess with him please. He is so nice !!! He knows a lot about a lot. In class he usually just lectures and his test and quiz are just based on the textbook and stuff we learned in class. It is not hard if you just study. I miss him everyday. One of the best teachers I had at Hunter and best class everrr ~~~
               <br/>
               <div class="submitted_by">
                <span class="hidden-xs">
                 Submitted by a student
                </span>
               </div>
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="26509037" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="26509037" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/26509037/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="26509037" style="display: none;">
             </div>
            </div>
           </div>
           <div class="ATF ad_container desktop-ad">
            <div class="ad-tag" data-ad-name="lead_desktop_2_teach" data-ad-size="728x90">
            </div>
           </div>
           <div class="col-xs-12 no_toggle review" id="rating_17436221" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r17436221">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="5.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 110.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="5.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2011-05-05" itemprop="datePublished">
               May 05, 2011
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               really funny and fair
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="17436221" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="17436221" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/17436221/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="17436221" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review secondary" id="rating_17242845" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r17242845">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val2 value">
               <span>
                2
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val2 value">
               <span>
                2
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="2.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 44.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="2.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2011-03-21" itemprop="datePublished">
               Mar 21, 2011
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               he lets you slack off, but he really doesn't know how to teach
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="1" data-id="17242845" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 1
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="1" data-id="17242845" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 1
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/17242845/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="17242845" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review" id="rating_16187973" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r16187973">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="5.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 110.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="5.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2010-09-11" itemprop="datePublished">
               Sep 11, 2010
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               You cant tell when he's serious and when he's not. You can't tell when he's about to blow the roof off and when he's just cracking a joke. So random. Epic teacher. =)
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="1" data-id="16187973" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 1
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="16187973" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/16187973/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="16187973" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review secondary" id="rating_15558500" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r15558500">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="4.5 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 99.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="4.5" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2010-05-10" itemprop="datePublished">
               May 10, 2010
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               hahhah he has TOWBER jokes. which arent funny most of the time... but he's cool :)
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="1" data-id="15558500" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 1
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="15558500" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/15558500/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="15558500" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review" id="rating_13376557" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r13376557">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val2 value">
               <span>
                2
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="3.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 66.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="3.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2008-04-12" itemprop="datePublished">
               Apr 12, 2008
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               He is very funny. Yeah i will say that he is corny. He is a little scary sometimes, but he is a good teacher. I like him alot.
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="1" data-id="13376557" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 1
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="2" data-id="13376557" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 2
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/13376557/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="13376557" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review secondary" id="rating_13121538" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r13121538">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="3.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 66.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="3.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2008-02-04" itemprop="datePublished">
               Feb 04, 2008
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               very corny - if you take a quiz you are a quizee...if you take a test you are a testee...overall an easy teacher
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="13121538" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="2" data-id="13121538" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 2
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/13121538/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="13121538" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review" id="rating_12886259" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r12886259">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="4.5 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 99.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="4.5" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2007-12-04" itemprop="datePublished">
               Dec 04, 2007
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               You can fail all of his homeworks, tests, and quizzes, but he'll still give you a good grade like A+. Also very hormonial, changes from trying to be funny to outrageously mad back to being funny. : )
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="1" data-id="12886259" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 1
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="1" data-id="12886259" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 1
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/12886259/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="12886259" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review secondary" id="rating_12865292" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r12865292">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="4.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 88.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="4.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2007-11-28" itemprop="datePublished">
               Nov 28, 2007
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               His a good teacher overall, but i can never tell whether his answers are serious
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="12865292" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="2" data-id="12865292" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 2
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/12865292/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="12865292" style="display: none;">
             </div>
            </div>
           </div>
           <div class="placements" style="border: 1px solid transparent;">
           </div>
           <div class="col-xs-12 no_toggle review" id="rating_12807388" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r12807388">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="4.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 88.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="4.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2007-11-11" itemprop="datePublished">
               Nov 11, 2007
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               hard tests, but easy studio grader. corny jokes, hates the French, is VERY SCARY. Still, he's mad cool.
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="12807388" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="12807388" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/12807388/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="12807388" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review secondary" id="rating_12802652" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r12802652">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="4.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 88.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="4.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2007-11-10" itemprop="datePublished">
               Nov 10, 2007
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               He's a pretty good teacher. Yes - the corny jokes, but generally, he's pretty funny and a good art teacher
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="12802652" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="1" data-id="12802652" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 1
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/12802652/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="12802652" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review" id="rating_12717759" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r12717759">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="3.5 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 77.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="3.5" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2007-10-16" itemprop="datePublished">
               Oct 16, 2007
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               awesome teacher. he basically gives u a good grade no matter what. i got an 80 on a test and a b- on my final report but still got an A in his class. corny jokes but is really funny and helpfull
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="12717759" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="1" data-id="12717759" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 1
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/12717759/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="12717759" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review secondary" id="rating_11888054" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r11888054">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="3.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 66.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="3.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2007-02-20" itemprop="datePublished">
               Feb 20, 2007
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               he hates the french and makes imitations.
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="11888054" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="11888054" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/11888054/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="11888054" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review" id="rating_11790241" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r11790241">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="4.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 88.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="4.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2007-01-30" itemprop="datePublished">
               Jan 30, 2007
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               i dont know how you cant love him. yes, he does make corny jokes, but he is a good teacher.
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="11790241" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="11790241" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/11790241/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="11790241" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review secondary" id="rating_11625828" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r11625828">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="4.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 88.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="4.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2006-12-19" itemprop="datePublished">
               Dec 19, 2006
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               So mean, and he's always making fun of me and my name.
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="1" data-id="11625828" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 1
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="11625828" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/11625828/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="11625828" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review" id="rating_11297327" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r11297327">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val2 value">
               <span>
                2
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val1 value">
               <span>
                1
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="2.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 44.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="2.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2006-11-14" itemprop="datePublished">
               Nov 14, 2006
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               Hilarious, but if you ask him a serious question, there's no guarantee how serious his answer is. I hated that class (partially that, partially because I don't like art class in general)
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="1" data-id="11297327" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 1
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="11297327" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/11297327/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="11297327" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review secondary" id="rating_11190403" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r11190403">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val2 value">
               <span>
                2
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="3.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 66.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="3.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2006-09-06" itemprop="datePublished">
               Sep 06, 2006
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               mr towber's jokes are really corny. but he's a fun teacher. easy grader even if you're not good at art. easy to space out during slideshows but u need the notes to pass the tests. cool dude.
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="11190403" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="11190403" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/11190403/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="11190403" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review" id="rating_10747058" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r10747058">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="4.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 88.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="4.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2006-05-03" itemprop="datePublished">
               May 03, 2006
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               omg, corny jokes but double art periods just gave us time to hang out and talk nonstop with friends. he can do hilarious beevis &amp; butthead impressions, but don't laugh too much about the buttress or stoopa jokes...
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="10747058" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="10747058" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/10747058/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="10747058" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review secondary" id="rating_10402836" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r10402836">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="4.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 88.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="4.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2006-02-15" itemprop="datePublished">
               Feb 15, 2006
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               Corny but hilarious jokes. Keeps on changing his first name. Can't ever tell if he's serious or not. Can't ever know for sure if he was joking or being serious. But nevertheless, Art was my most favorite class.
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="10402836" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="10402836" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/10402836/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="10402836" style="display: none;">
             </div>
            </div>
           </div>
           <div class="placements" style="border: 1px solid transparent;">
           </div>
           <div class="col-xs-12 no_toggle review" id="rating_10033961" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r10033961">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="5.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 110.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="5.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2005-12-03" itemprop="datePublished">
               Dec 03, 2005
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               I cant really draw and he likes my work. Makes the history cool with jokes and news reports. Keeps me awake after boring english.
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="10033961" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="10033961" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/10033961/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="10033961" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review secondary" id="rating_9825380" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r9825380">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="3.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 66.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="3.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2005-10-26" itemprop="datePublished">
               Oct 26, 2005
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="9825380" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="9825380" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/9825380/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="9825380" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review" id="rating_9792756" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r9792756">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="3.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 66.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="3.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2005-10-20" itemprop="datePublished">
               Oct 20, 2005
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               Easy work
and good comebacks too
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="9792756" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="9792756" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/9792756/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="9792756" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review secondary" id="rating_9790514" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r9790514">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val2 value">
               <span>
                2
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="3.5 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 77.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="3.5" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2005-10-20" itemprop="datePublished">
               Oct 20, 2005
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               It's DISCIPLINE TOWBER. Not David. Pretty funny teacher, easy too, though he would not have you believe that...
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="9790514" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="9790514" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/9790514/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="9790514" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review" id="rating_9695072" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r9695072">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="4.5 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 99.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="4.5" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2005-10-02" itemprop="datePublished">
               Oct 02, 2005
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               he's an awesome teacher. he has a really funky sense of humor and can get really sarcastic at times, but that just makes his class even more interesting.
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="9695072" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="9695072" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/9695072/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="9695072" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review secondary" id="rating_9580140" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r9580140">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val2 value">
               <span>
                2
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="2.5 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 55.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="2.5" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2005-09-13" itemprop="datePublished">
               Sep 13, 2005
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               hes okay but makes corny jokes and i'm not sure whether to take him seriously or not... but not that bad, i guess
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="9580140" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="9580140" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/9580140/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="9580140" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review" id="rating_8869288" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r8869288">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="4.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 88.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="4.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2005-04-30" itemprop="datePublished">
               Apr 30, 2005
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               what a confusing personality.. sometimes mean w/ us and Rosenberg, and sometimes accepting term papers weeks late (it wasnt me, mr towber)
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="8869288" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="8869288" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/8869288/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="8869288" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review secondary" id="rating_8360235" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r8360235">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="5.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 110.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="5.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2005-02-21" itemprop="datePublished">
               Feb 21, 2005
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               SUCH a favoritist. Seriously, I drew this crappy stick figure Baldwins Mansion for the Chinese thing and got an A+. He was so funny, and he'll love you if you joke with him.
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="8360235" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="8360235" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/8360235/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="8360235" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review" id="rating_7786594" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r7786594">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="5.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 110.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="5.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2004-12-11" itemprop="datePublished">
               Dec 11, 2004
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               knows the students, funny, what more can i say?
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="7786594" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="7786594" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/7786594/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="7786594" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review secondary" id="rating_7782622" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r7782622">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="5.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 110.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="5.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2004-12-10" itemprop="datePublished">
               Dec 10, 2004
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               Likes to joke a lot but knows his stuff and does cool art.
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="7782622" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="7782622" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/7782622/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="7782622" style="display: none;">
             </div>
            </div>
           </div>
           <div class="placements" style="border: 1px solid transparent;">
           </div>
           <div class="col-xs-12 no_toggle review" id="rating_7680657" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r7680657">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="3.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 66.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="3.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2004-11-30" itemprop="datePublished">
               Nov 30, 2004
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               when i walked into his art room and i heard him speak, i knew i was in for a year of corny jokes and funky projects. Wierd guy.... he is ez on hw,no due dates
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="7680657" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="7680657" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/7680657/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="7680657" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review secondary" id="rating_7631915" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r7631915">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="4.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 88.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="4.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2004-11-22" itemprop="datePublished">
               Nov 22, 2004
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               laugh and you'll pass, curses but hes better than 99% of the teachers
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="1" data-id="7631915" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 1
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="7631915" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/7631915/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="7631915" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review" id="rating_7273629" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r7273629">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="4.5 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 99.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="4.5" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2004-10-08" itemprop="datePublished">
               Oct 08, 2004
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               Mr. Towber is histerical, he is the funniest teacher I ever had, all he does is make fun of people, he awesome!!
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="7273629" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="7273629" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/7273629/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="7273629" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review secondary" id="rating_7218205" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r7218205">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="3.5 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 77.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="3.5" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2004-09-30" itemprop="datePublished">
               Sep 30, 2004
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               He's a great teacher! Most of his jokes are funny, although they're all corny. I love art class!
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="7218205" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="7218205" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/7218205/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="7218205" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review" id="rating_7143125" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r7143125">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="5.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 110.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="5.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2004-09-17" itemprop="datePublished">
               Sep 17, 2004
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               mr towber is really good. he cant draw well, but he grades fairly and knows most of the art. hes also really funny.
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="7143125" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="7143125" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/7143125/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="7143125" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review secondary" id="rating_6741711" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r6741711">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="5.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 110.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="5.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2004-06-24" itemprop="datePublished">
               Jun 24, 2004
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               how could u not like this guy? really funny, and helpful. cool teacher
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="6741711" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="6741711" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/6741711/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="6741711" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review" id="rating_5320284" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r5320284">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="5.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 110.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="5.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2004-03-04" itemprop="datePublished">
               Mar 04, 2004
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               i dinq i wus a favorite of his. he's really nice.
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="5320284" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="5320284" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/5320284/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="5320284" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review secondary" id="rating_4833897" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r4833897">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="5.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 110.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="5.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2004-02-05" itemprop="datePublished">
               Feb 05, 2004
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               Makes lotsa jokes. Is pretty sarcastic a lot. Hes always chill with Rosenberg and Kissack and very funny. Good art history teacher and general artist too.
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="4833897" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="4833897" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/4833897/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="4833897" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review" id="rating_2487840" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r2487840">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val1 value">
               <span>
                1
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="2.5 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 55.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="2.5" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2003-06-13" itemprop="datePublished">
               Jun 13, 2003
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               He has problems...his jokes are really corny..
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="2487840" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="2487840" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/2487840/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="2487840" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review secondary" id="rating_1350068" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r1350068">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val2 value">
               <span>
                2
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="2.5 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 55.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="2.5" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2003-06-06" itemprop="datePublished">
               Jun 06, 2003
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               he's scary sometimes as a teacher but when he visits us in Rosenberg's class.....he's fun. Me and my best friend call him Davie.
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="1350068" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="1350068" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/1350068/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="1350068" style="display: none;">
             </div>
            </div>
           </div>
           <div class="placements" style="border: 1px solid transparent;">
           </div>
           <div class="col-xs-12 no_toggle review" id="rating_2350947" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r2350947">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="3.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 66.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="3.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2003-06-02" itemprop="datePublished">
               Jun 02, 2003
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               Good photo teacher, but kinda difficult, just cuz it's so hard to tell whether he's serious about his critiques or just joking around.
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="2350947" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="2350947" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/2350947/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="2350947" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review secondary" id="rating_1933141" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r1933141">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="3.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 66.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="3.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2003-05-05" itemprop="datePublished">
               May 05, 2003
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               Yeah... Corny jokes, but hey he's a teacher in Hunter, can you help it? His classes are easy enough to pass.
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="1933141" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="1933141" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/1933141/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="1933141" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review" id="rating_1889522" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r1889522">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val1 value">
               <span>
                1
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val2 value">
               <span>
                2
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="1.5 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 33.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="1.5" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2003-05-02" itemprop="datePublished">
               May 02, 2003
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               No one likes him. Bad jokes.
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="1" data-id="1889522" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 1
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="1889522" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/1889522/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="1889522" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review secondary" id="rating_1828006" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r1828006">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="4.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 88.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="4.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2003-04-27" itemprop="datePublished">
               Apr 27, 2003
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               Love him, love him, love him. He once gave a test with 32 points of extra credit. People still managed to get 74s (I'm not sure how). Anyway, he's really fun
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="1828006" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="1828006" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/1828006/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="1828006" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review" id="rating_1535762" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r1535762">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="4.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 88.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="4.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2003-04-06" itemprop="datePublished">
               Apr 06, 2003
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               He makes conry jokes...just laugh and try your best when you draw he's lenient with the drawings and stuff take notes when he says take notes. He teaches well.
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="1535762" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="1535762" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/1535762/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="1535762" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review secondary" id="rating_1522901" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r1522901">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="4.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 88.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="4.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2003-04-05" itemprop="datePublished">
               Apr 05, 2003
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               hes the most easiest teacher in the world..his jokes can sumtimes get annoying and corny, but hes really nice. i dunt understand y ppl dont lik him
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="1522901" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="1522901" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/1522901/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="1522901" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review" id="rating_1522346" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r1522346">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val5 value">
               <span>
                5
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val1 value">
               <span>
                1
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val2 value">
               <span>
                2
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="1.5 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 33.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="1.5" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2003-04-05" itemprop="datePublished">
               Apr 05, 2003
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               He makes really corny, unfunny jokes and hes mean. Mean mean mean. Grr
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="2" data-id="1522346" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 2
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="1522346" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/1522346/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="1522346" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review secondary" id="rating_1479227" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r1479227">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="3.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 66.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="3.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2003-04-03" itemprop="datePublished">
               Apr 03, 2003
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               most awesome teacher ever sooooo funny hah i loved him cept hes sometimes *err* serious...
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="1479227" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="1479227" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/1479227/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="1479227" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review" id="rating_1419971" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r1419971">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="4.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 88.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="4.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2003-03-31" itemprop="datePublished">
               Mar 31, 2003
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               He is just like Mr.Rosenburg but he can be scary because you never know when he lying, serious or what.
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="1" data-id="1419971" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 1
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="1419971" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/1419971/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="1419971" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review secondary" id="rating_1395586" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r1395586">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="3.5 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 77.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="3.5" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2003-03-29" itemprop="datePublished">
               Mar 29, 2003
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               weird kinda cool.
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="0" data-id="1395586" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 0
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="1" data-id="1395586" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 1
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/1395586/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="1395586" style="display: none;">
             </div>
            </div>
           </div>
           <div class="placements" style="border: 1px solid transparent;">
           </div>
           <div class="col-xs-12 no_toggle review" id="rating_1357775" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r1357775">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="4.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 88.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="4.0" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2003-03-27" itemprop="datePublished">
               Mar 27, 2003
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               High all the time
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="1" data-id="1357775" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 1
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="1357775" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/1357775/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="1357775" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 no_toggle review secondary" id="rating_1225783" itemprop="review" itemscope="" itemtype="https://schema.org/Review">
            <meta content="RateMyTeachers User" itemprop="author"/>
            <a name="r1225783">
            </a>
            <div class="col-xs-4 col-lg-3 attributes">
             <div class="attribute">
              <div class="easy val4 value">
               <span>
                4
               </span>
              </div>
              <div class="text">
               Easiness
              </div>
             </div>
             <div class="attribute">
              <div class="helpful val2 value">
               <span>
                2
               </span>
              </div>
              <div class="text">
               Helpfulness
              </div>
             </div>
             <div class="attribute">
              <div class="clarity val3 value">
               <span>
                3
               </span>
              </div>
              <div class="text">
               Clarity
              </div>
             </div>
            </div>
            <div class="col-xs-8 col-lg-9 details">
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="2.5 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 55.000px;">
                </div>
               </div>
              </div>
              <span class="dn" itemprop="reviewRating" itemscope="" itemtype="https://schema.org/Rating">
               <meta content="0" itemprop="worstRating"/>
               <meta content="5" itemprop="bestRating"/>
               <meta content="2.5" itemprop="ratingValue"/>
              </span>
              <span class="date" datetime="2003-03-16" itemprop="datePublished">
               Mar 16, 2003
              </span>
             </div>
             <p class="comments">
              <span class="text" itemprop="description">
               i did well in his class since art is one of my better subjects, but hes not that easy.
              </span>
             </p>
             <div class="options">
              <div class="thumbs thumb_container rating_thumbs">
               <a class="thumb_score thumb_trigger up" data-count="1" data-id="1225783" data-type="up" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-up">
                </i>
                <div class="value">
                 1
                </div>
               </a>
               <a class="down thumb_score thumb_trigger" data-count="0" data-id="1225783" data-type="down" href="javascript:void(0);">
                <i class="fa fa-thumbs-o-down">
                </i>
                <div class="value">
                 0
                </div>
               </a>
              </div>
              <a class="btn edit flag_rating_trigger" data-remote="/ratings/1225783/flag" data-sender-name="Teacher page Ratings List" data-target="#modal" data-teacher="David Towber" data-toggle="modal" href="javascript:;" rel="nofollow" remote="" title="Flag Rating for David Towber">
               <span>
                <i class="fa fa-flag">
                </i>
                Flag
               </span>
              </a>
             </div>
             <div class="rating_actions" data-rid="1225783" style="display: none;">
             </div>
            </div>
           </div>
           <div class="col-xs-12 ad_container BTF">
            <div class="sponsor">
             <div class="ad-tag" data-ad-name="lead_desktop_3_teach" data-ad-size="728x90">
             </div>
            </div>
           </div>
           <div class="col-xs-12 similar_department_teachers">
            <h2 class="col-xs-12 subtitle">
             Similar visual arts teachers like David Towber?
            </h2>
            <div class="col-xs-12">
             <div class="col-xs-6 teachers">
              <div class="row item">
               <div class="col-xs-7 title_container">
                <a alt="View Constance Rich's Ratings" class="teacher_name" href="/constance-rich/193686-t" title="View Constance Rich's Ratings">
                 Constance Rich
                </a>
                <span class="position">
                 Visual Arts
                </span>
               </div>
               <div class="col-xs-5 score">
                <div class="rateit star-rating rateit-exclude" title="4.6 of 5">
                 <div class="rateit-range" style="width: 90px; height: 15px;">
                  <div class="rateit-preset rateit-selected" style="height: 15px; width: 82.440px;">
                  </div>
                 </div>
                </div>
                40
Ratings
               </div>
              </div>
              <div class="row item">
               <div class="col-xs-7 title_container">
                <a alt="View Julie Reifer's Ratings" class="teacher_name" href="/julie-reifer/239002-t" title="View Julie Reifer's Ratings">
                 Julie Reifer
                </a>
                <span class="position">
                 Visual Arts
                </span>
               </div>
               <div class="col-xs-5 score">
                <div class="rateit star-rating rateit-exclude" title="4.0 of 5">
                 <div class="rateit-range" style="width: 90px; height: 15px;">
                  <div class="rateit-preset rateit-selected" style="height: 15px; width: 72.360px;">
                  </div>
                 </div>
                </div>
                18
Ratings
               </div>
              </div>
              <div class="row item">
               <div class="col-xs-7 title_container">
                <a alt="View Eve Eisenstadt's Ratings" class="teacher_name" href="/eve-eisenstadt/246828-t" title="View Eve Eisenstadt's Ratings">
                 Eve Eisenstadt
                </a>
                <span class="position">
                 Visual Arts
                </span>
               </div>
               <div class="col-xs-5 score">
                <div class="rateit star-rating rateit-exclude" title="3.8 of 5">
                 <div class="rateit-range" style="width: 90px; height: 15px;">
                  <div class="rateit-preset rateit-selected" style="height: 15px; width: 69.120px;">
                  </div>
                 </div>
                </div>
                16
Ratings
               </div>
              </div>
              <div class="row item">
               <div class="col-xs-7 title_container">
                <a alt="View Lauren Quigley's Ratings" class="teacher_name" href="/lauren-quigley/2283419-t" title="View Lauren Quigley's Ratings">
                 Lauren Quigley
                </a>
                <span class="position">
                 Visual Arts
                </span>
               </div>
               <div class="col-xs-5 score">
                <div class="rateit star-rating rateit-exclude" title="4.3 of 5">
                 <div class="rateit-range" style="width: 90px; height: 15px;">
                  <div class="rateit-preset rateit-selected" style="height: 15px; width: 76.860px;">
                  </div>
                 </div>
                </div>
                5
Ratings
               </div>
              </div>
              <div class="row item">
               <div class="col-xs-7 title_container">
                <a alt="View Joanne Ellis' Ratings" class="teacher_name" href="/joanne-ellis/2310374-t" title="View Joanne Ellis' Ratings">
                 Joanne Ellis
                </a>
                <span class="position">
                 Visual Arts
                </span>
               </div>
               <div class="col-xs-5 score">
                <div class="rateit star-rating rateit-exclude" title="2.5 of 5">
                 <div class="rateit-range" style="width: 90px; height: 15px;">
                  <div class="rateit-preset rateit-selected" style="height: 15px; width: 45.000px;">
                  </div>
                 </div>
                </div>
                2
Ratings
               </div>
              </div>
             </div>
             <div class="col-xs-6 ad_container MID_rectangle">
              <div class="ad-tag" data-ad-name="mrec_desktop_teach" data-ad-size="300x250">
              </div>
             </div>
            </div>
           </div>
           <div class="col-xs-12 pagination_container">
            <div class="back_button_new_theme ">
             <a href="/hunter-college-high-school/25767-s" title="View Hunter College High School's Teachers">
              Back to Teachers at Hunter College High School
             </a>
            </div>
            <div class="text">
             Page
1
of
1
            </div>
           </div>
          </div>
         </div>
         <div class="col-xs-3 secondary_column with_ads">
          <div class="ad_container ATF_rectangle sponsor">
           <div class="ad-tag" data-ad-name="teach_topright_mrec" data-ad-size="300x250">
           </div>
          </div>
          <div class="col-xs-12">
           <div class="row block_container school_card">
            <div class="col-xs-12">
             <h2 class="school_name" title="Learn more about Hunter College High School">
              <a class="school_name" href="/hunter-college-high-school/25767-s" title="Learn more about Hunter College High School">
               Learn more about Hunter College High School
              </a>
             </h2>
             <div class="score_line_container">
              <div class="score_label">
               5-star
              </div>
              <div class="score_percentage">
               69%
              </div>
              <div class="score_line">
               <div class="aux" style="width: 69.61%;">
               </div>
              </div>
             </div>
             <div class="score_line_container">
              <div class="score_label">
               4-star
              </div>
              <div class="score_percentage">
               14%
              </div>
              <div class="score_line">
               <div class="aux" style="width: 14.1%;">
               </div>
              </div>
             </div>
             <div class="score_line_container">
              <div class="score_label">
               3-star
              </div>
              <div class="score_percentage">
               8%
              </div>
              <div class="score_line">
               <div class="aux" style="width: 8.49%;">
               </div>
              </div>
             </div>
             <div class="score_line_container">
              <div class="score_label">
               2-star
              </div>
              <div class="score_percentage">
               2%
              </div>
              <div class="score_line">
               <div class="aux" style="width: 2.89%;">
               </div>
              </div>
             </div>
             <div class="score_line_container">
              <div class="score_label">
               1-star
              </div>
              <div class="score_percentage">
               4%
              </div>
              <div class="score_line">
               <div class="aux" style="width: 4.9%;">
               </div>
              </div>
             </div>
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="4.0 of 5">
               <div class="rateit-range" style="width: 90px; height: 15px;">
                <div class="rateit-preset rateit-selected" style="height: 15px; width: 71.517px;">
                </div>
               </div>
              </div>
              <span class="rating-summary">
               Based on
4,301
Ratings
              </span>
             </div>
            </div>
            <div class="col-xs-12 details">
             <strong>
              Hunter College High School
             </strong>
             is located in New York, New York
with an average teacher rating of 3.97
stars. When comparing
Hunter College High School's teachers to other
teachers in the state of
New York, Hunter College High School's
teachers are
below
the average of
4.39
stars.
Hunter College High School ranks
546
amongst all High Schools
in the state of New York.
             <a class="learn_more" href="/hunter-college-high-school/25767-s/stats" title="Go to Hunter College High School stats">
              Learn More
             </a>
            </div>
           </div>
          </div>
          <div class="col-xs-12 sticky_container_right">
           <div class="sticky_column">
            <div class="ad_container BTF_rectangle sponsor">
             <div class="ad-tag" data-ad-name="halfpage_desktop_teach_mrec" data-ad-size="300x250">
             </div>
             <script type="text/javascript">
              (deployads = window.deployads || []).push({});
             </script>
             <div id="div-gpt-ad-1429202442736-0" style="min-width: 300px; min-height: 250px;">
              <script type="text/javascript">
               _googlePush( function() { 
        // console.info('LazyAds: googletag.display Teacher5 div-gpt-ad-1429202442736-0');
        var slot = googletag.defineSlot('/1058149/Teacher5', [300,250], 'div-gpt-ad-1429202442736-0').addService(googletag.pubads());
        googletag.display('div-gpt-ad-1429202442736-0'); 
        googletag.pubads().refresh([slot]);

      }, 900 );
  
      if (!window.__ssrt_ab_is_them) {
        document.getElementById('div-gpt-ad-1429202442736-0').style.display = 'none';
      }
              </script>
             </div>
            </div>
           </div>
          </div>
         </div>
        </div>
       </section>
      </div>
     </div>
    </div>
   </div>
  </div>
  <div id="all_footer_wrapper" style="overflow:hidden;">
   <section class="container-fluid hidden-xs padding" id="states">
    <div class="container">
     <div class="row">
      <div class="col-xs-12 col-sm-12 col-sm-offset-0 footer_states_container">
       <h3>
        Locate Schools by State:
       </h3>
       <div class="states">
        <div class="state">
         <a alt="Find Alaska's High Schools and Colleges" href="/alaska" title="Find Alaska's High Schools and Colleges">
          Alaska
         </a>
        </div>
        <div class="state">
         <a alt="Find Alabama's High Schools and Colleges" href="/alabama" title="Find Alabama's High Schools and Colleges">
          Alabama
         </a>
        </div>
        <div class="state">
         <a alt="Find Arkansas' High Schools and Colleges" href="/arkansas" title="Find Arkansas' High Schools and Colleges">
          Arkansas
         </a>
        </div>
        <div class="state">
         <a alt="Find Arizona's High Schools and Colleges" href="/arizona" title="Find Arizona's High Schools and Colleges">
          Arizona
         </a>
        </div>
        <div class="state">
         <a alt="Find California's High Schools and Colleges" href="/california" title="Find California's High Schools and Colleges">
          California
         </a>
        </div>
        <div class="state">
         <a alt="Find Colorado's High Schools and Colleges" href="/colorado" title="Find Colorado's High Schools and Colleges">
          Colorado
         </a>
        </div>
        <div class="state">
         <a alt="Find Connecticut's High Schools and Colleges" href="/connecticut" title="Find Connecticut's High Schools and Colleges">
          Connecticut
         </a>
        </div>
        <div class="state">
         <a alt="Find DC's High Schools and Colleges" href="/dc" title="Find DC's High Schools and Colleges">
          DC
         </a>
        </div>
        <div class="state">
         <a alt="Find Delaware's High Schools and Colleges" href="/delaware" title="Find Delaware's High Schools and Colleges">
          Delaware
         </a>
        </div>
        <div class="state">
         <a alt="Find Florida's High Schools and Colleges" href="/florida" title="Find Florida's High Schools and Colleges">
          Florida
         </a>
        </div>
        <div class="state">
         <a alt="Find Georgia's High Schools and Colleges" href="/georgia" title="Find Georgia's High Schools and Colleges">
          Georgia
         </a>
        </div>
        <div class="state">
         <a alt="Find Hawaii's High Schools and Colleges" href="/hawaii" title="Find Hawaii's High Schools and Colleges">
          Hawaii
         </a>
        </div>
        <div class="state">
         <a alt="Find Iowa's High Schools and Colleges" href="/iowa" title="Find Iowa's High Schools and Colleges">
          Iowa
         </a>
        </div>
        <div class="state">
         <a alt="Find Idaho's High Schools and Colleges" href="/idaho" title="Find Idaho's High Schools and Colleges">
          Idaho
         </a>
        </div>
        <div class="state">
         <a alt="Find Illinois' High Schools and Colleges" href="/illinois" title="Find Illinois' High Schools and Colleges">
          Illinois
         </a>
        </div>
        <div class="state">
         <a alt="Find Indiana's High Schools and Colleges" href="/indiana" title="Find Indiana's High Schools and Colleges">
          Indiana
         </a>
        </div>
        <div class="state">
         <a alt="Find Kansas' High Schools and Colleges" href="/kansas" title="Find Kansas' High Schools and Colleges">
          Kansas
         </a>
        </div>
        <div class="state">
         <a alt="Find Kentucky's High Schools and Colleges" href="/kentucky" title="Find Kentucky's High Schools and Colleges">
          Kentucky
         </a>
        </div>
        <div class="state">
         <a alt="Find Louisiana's High Schools and Colleges" href="/louisiana" title="Find Louisiana's High Schools and Colleges">
          Louisiana
         </a>
        </div>
        <div class="state">
         <a alt="Find Massachusetts' High Schools and Colleges" href="/massachusetts" title="Find Massachusetts' High Schools and Colleges">
          Massachusetts
         </a>
        </div>
        <div class="state">
         <a alt="Find Maryland's High Schools and Colleges" href="/maryland" title="Find Maryland's High Schools and Colleges">
          Maryland
         </a>
        </div>
        <div class="state">
         <a alt="Find Maine's High Schools and Colleges" href="/maine" title="Find Maine's High Schools and Colleges">
          Maine
         </a>
        </div>
        <div class="state">
         <a alt="Find Michigan's High Schools and Colleges" href="/michigan" title="Find Michigan's High Schools and Colleges">
          Michigan
         </a>
        </div>
        <div class="state">
         <a alt="Find Minnesota's High Schools and Colleges" href="/minnesota" title="Find Minnesota's High Schools and Colleges">
          Minnesota
         </a>
        </div>
        <div class="state">
         <a alt="Find Missouri's High Schools and Colleges" href="/missouri" title="Find Missouri's High Schools and Colleges">
          Missouri
         </a>
        </div>
        <div class="state">
         <a alt="Find Mississippi's High Schools and Colleges" href="/mississippi" title="Find Mississippi's High Schools and Colleges">
          Mississippi
         </a>
        </div>
        <div class="state">
         <a alt="Find Montana's High Schools and Colleges" href="/montana" title="Find Montana's High Schools and Colleges">
          Montana
         </a>
        </div>
        <div class="state">
         <a alt="Find North Carolina's High Schools and Colleges" href="/north-carolina" title="Find North Carolina's High Schools and Colleges">
          North Carolina
         </a>
        </div>
        <div class="state">
         <a alt="Find North Dakota's High Schools and Colleges" href="/north-dakota" title="Find North Dakota's High Schools and Colleges">
          North Dakota
         </a>
        </div>
        <div class="state">
         <a alt="Find Nebraska's High Schools and Colleges" href="/nebraska" title="Find Nebraska's High Schools and Colleges">
          Nebraska
         </a>
        </div>
        <div class="state">
         <a alt="Find New Hampshire's High Schools and Colleges" href="/new-hampshire" title="Find New Hampshire's High Schools and Colleges">
          New Hampshire
         </a>
        </div>
        <div class="state">
         <a alt="Find New Jersey's High Schools and Colleges" href="/new-jersey" title="Find New Jersey's High Schools and Colleges">
          New Jersey
         </a>
        </div>
        <div class="state">
         <a alt="Find New Mexico's High Schools and Colleges" href="/new-mexico" title="Find New Mexico's High Schools and Colleges">
          New Mexico
         </a>
        </div>
        <div class="state">
         <a alt="Find Nevada's High Schools and Colleges" href="/nevada" title="Find Nevada's High Schools and Colleges">
          Nevada
         </a>
        </div>
        <div class="state">
         <a alt="Find New York's High Schools and Colleges" href="/new-york" title="Find New York's High Schools and Colleges">
          New York
         </a>
        </div>
        <div class="state">
         <a alt="Find Ohio's High Schools and Colleges" href="/ohio" title="Find Ohio's High Schools and Colleges">
          Ohio
         </a>
        </div>
        <div class="state">
         <a alt="Find Oklahoma's High Schools and Colleges" href="/oklahoma" title="Find Oklahoma's High Schools and Colleges">
          Oklahoma
         </a>
        </div>
        <div class="state">
         <a alt="Find Oregon's High Schools and Colleges" href="/oregon" title="Find Oregon's High Schools and Colleges">
          Oregon
         </a>
        </div>
        <div class="state">
         <a alt="Find Pennsylvania's High Schools and Colleges" href="/pennsylvania" title="Find Pennsylvania's High Schools and Colleges">
          Pennsylvania
         </a>
        </div>
        <div class="state">
         <a alt="Find Puerto Rico's High Schools and Colleges" href="/puerto-rico" title="Find Puerto Rico's High Schools and Colleges">
          Puerto Rico
         </a>
        </div>
        <div class="state">
         <a alt="Find Rhode Island's High Schools and Colleges" href="/rhode-island" title="Find Rhode Island's High Schools and Colleges">
          Rhode Island
         </a>
        </div>
        <div class="state">
         <a alt="Find South Carolina's High Schools and Colleges" href="/south-carolina" title="Find South Carolina's High Schools and Colleges">
          South Carolina
         </a>
        </div>
        <div class="state">
         <a alt="Find South Dakota's High Schools and Colleges" href="/south-dakota" title="Find South Dakota's High Schools and Colleges">
          South Dakota
         </a>
        </div>
        <div class="state">
         <a alt="Find Tennessee's High Schools and Colleges" href="/tennessee" title="Find Tennessee's High Schools and Colleges">
          Tennessee
         </a>
        </div>
        <div class="state">
         <a alt="Find Texas' High Schools and Colleges" href="/texas" title="Find Texas' High Schools and Colleges">
          Texas
         </a>
        </div>
        <div class="state">
         <a alt="Find Utah's High Schools and Colleges" href="/utah" title="Find Utah's High Schools and Colleges">
          Utah
         </a>
        </div>
        <div class="state">
         <a alt="Find Virginia's High Schools and Colleges" href="/virginia" title="Find Virginia's High Schools and Colleges">
          Virginia
         </a>
        </div>
        <div class="state">
         <a alt="Find Vermont's High Schools and Colleges" href="/vermont" title="Find Vermont's High Schools and Colleges">
          Vermont
         </a>
        </div>
        <div class="state">
         <a alt="Find Washington's High Schools and Colleges" href="/washington" title="Find Washington's High Schools and Colleges">
          Washington
         </a>
        </div>
        <div class="state">
         <a alt="Find Wisconsin's High Schools and Colleges" href="/wisconsin" title="Find Wisconsin's High Schools and Colleges">
          Wisconsin
         </a>
        </div>
        <div class="state">
         <a alt="Find West Virginia's High Schools and Colleges" href="/west-virginia" title="Find West Virginia's High Schools and Colleges">
          West Virginia
         </a>
        </div>
        <div class="state">
         <a alt="Find Wyoming's High Schools and Colleges" href="/wyoming" title="Find Wyoming's High Schools and Colleges">
          Wyoming
         </a>
        </div>
       </div>
      </div>
     </div>
    </div>
   </section>
   <section class="container-fluid" id="footer_directory">
    <div class="container">
     <div class="row">
      <div class="col-xs-6 hidden-xs">
       High School and College Directory:
       <a alt='Schools beginning with "A"' href="/schools/directory/a" title='Schools beginning with "A"'>
        a
       </a>
       <a alt='Schools beginning with "B"' href="/schools/directory/b" title='Schools beginning with "B"'>
        b
       </a>
       <a alt='Schools beginning with "C"' href="/schools/directory/c" title='Schools beginning with "C"'>
        c
       </a>
       <a alt='Schools beginning with "D"' href="/schools/directory/d" title='Schools beginning with "D"'>
        d
       </a>
       <a alt='Schools beginning with "E"' href="/schools/directory/e" title='Schools beginning with "E"'>
        e
       </a>
       <a alt='Schools beginning with "F"' href="/schools/directory/f" title='Schools beginning with "F"'>
        f
       </a>
       <a alt='Schools beginning with "G"' href="/schools/directory/g" title='Schools beginning with "G"'>
        g
       </a>
       <a alt='Schools beginning with "H"' href="/schools/directory/h" title='Schools beginning with "H"'>
        h
       </a>
       <a alt='Schools beginning with "I"' href="/schools/directory/i" title='Schools beginning with "I"'>
        i
       </a>
       <a alt='Schools beginning with "J"' href="/schools/directory/j" title='Schools beginning with "J"'>
        j
       </a>
       <a alt='Schools beginning with "K"' href="/schools/directory/k" title='Schools beginning with "K"'>
        k
       </a>
       <a alt='Schools beginning with "L"' href="/schools/directory/l" title='Schools beginning with "L"'>
        l
       </a>
       <a alt='Schools beginning with "M"' href="/schools/directory/m" title='Schools beginning with "M"'>
        m
       </a>
       <a alt='Schools beginning with "N"' href="/schools/directory/n" title='Schools beginning with "N"'>
        n
       </a>
       <a alt='Schools beginning with "O"' href="/schools/directory/o" title='Schools beginning with "O"'>
        o
       </a>
       <a alt='Schools beginning with "P"' href="/schools/directory/p" title='Schools beginning with "P"'>
        p
       </a>
       <a alt='Schools beginning with "Q"' href="/schools/directory/q" title='Schools beginning with "Q"'>
        q
       </a>
       <a alt='Schools beginning with "R"' href="/schools/directory/r" title='Schools beginning with "R"'>
        r
       </a>
       <a alt='Schools beginning with "S"' href="/schools/directory/s" title='Schools beginning with "S"'>
        s
       </a>
       <a alt='Schools beginning with "T"' href="/schools/directory/t" title='Schools beginning with "T"'>
        t
       </a>
       <a alt='Schools beginning with "U"' href="/schools/directory/u" title='Schools beginning with "U"'>
        u
       </a>
       <a alt='Schools beginning with "V"' href="/schools/directory/v" title='Schools beginning with "V"'>
        v
       </a>
       <a alt='Schools beginning with "W"' href="/schools/directory/w" title='Schools beginning with "W"'>
        w
       </a>
       <a alt='Schools beginning with "X"' href="/schools/directory/x" title='Schools beginning with "X"'>
        x
       </a>
       <a alt='Schools beginning with "Y"' href="/schools/directory/y" title='Schools beginning with "Y"'>
        y
       </a>
       <a alt='Schools beginning with "Z"' href="/schools/directory/z" title='Schools beginning with "Z"'>
        z
       </a>
       <a alt="Schools beginning with numbers" href="/schools/directory/%23" title="Schools beginning with numbers">
        #
       </a>
      </div>
      <div class="col-xs-6 hidden-xs">
       Teacher and Professor Directory:
       <a alt='Teachers beginning with "A"' href="/teachers/directory/a" title='Teachers beginning with "A"'>
        a
       </a>
       <a alt='Teachers beginning with "B"' href="/teachers/directory/b" title='Teachers beginning with "B"'>
        b
       </a>
       <a alt='Teachers beginning with "C"' href="/teachers/directory/c" title='Teachers beginning with "C"'>
        c
       </a>
       <a alt='Teachers beginning with "D"' href="/teachers/directory/d" title='Teachers beginning with "D"'>
        d
       </a>
       <a alt='Teachers beginning with "E"' href="/teachers/directory/e" title='Teachers beginning with "E"'>
        e
       </a>
       <a alt='Teachers beginning with "F"' href="/teachers/directory/f" title='Teachers beginning with "F"'>
        f
       </a>
       <a alt='Teachers beginning with "G"' href="/teachers/directory/g" title='Teachers beginning with "G"'>
        g
       </a>
       <a alt='Teachers beginning with "H"' href="/teachers/directory/h" title='Teachers beginning with "H"'>
        h
       </a>
       <a alt='Teachers beginning with "I"' href="/teachers/directory/i" title='Teachers beginning with "I"'>
        i
       </a>
       <a alt='Teachers beginning with "J"' href="/teachers/directory/j" title='Teachers beginning with "J"'>
        j
       </a>
       <a alt='Teachers beginning with "K"' href="/teachers/directory/k" title='Teachers beginning with "K"'>
        k
       </a>
       <a alt='Teachers beginning with "L"' href="/teachers/directory/l" title='Teachers beginning with "L"'>
        l
       </a>
       <a alt='Teachers beginning with "M"' href="/teachers/directory/m" title='Teachers beginning with "M"'>
        m
       </a>
       <a alt='Teachers beginning with "N"' href="/teachers/directory/n" title='Teachers beginning with "N"'>
        n
       </a>
       <a alt='Teachers beginning with "O"' href="/teachers/directory/o" title='Teachers beginning with "O"'>
        o
       </a>
       <a alt='Teachers beginning with "P"' href="/teachers/directory/p" title='Teachers beginning with "P"'>
        p
       </a>
       <a alt='Teachers beginning with "Q"' href="/teachers/directory/q" title='Teachers beginning with "Q"'>
        q
       </a>
       <a alt='Teachers beginning with "R"' href="/teachers/directory/r" title='Teachers beginning with "R"'>
        r
       </a>
       <a alt='Teachers beginning with "S"' href="/teachers/directory/s" title='Teachers beginning with "S"'>
        s
       </a>
       <a alt='Teachers beginning with "T"' href="/teachers/directory/t" title='Teachers beginning with "T"'>
        t
       </a>
       <a alt='Teachers beginning with "U"' href="/teachers/directory/u" title='Teachers beginning with "U"'>
        u
       </a>
       <a alt='Teachers beginning with "V"' href="/teachers/directory/v" title='Teachers beginning with "V"'>
        v
       </a>
       <a alt='Teachers beginning with "W"' href="/teachers/directory/w" title='Teachers beginning with "W"'>
        w
       </a>
       <a alt='Teachers beginning with "X"' href="/teachers/directory/x" title='Teachers beginning with "X"'>
        x
       </a>
       <a alt='Teachers beginning with "Y"' href="/teachers/directory/y" title='Teachers beginning with "Y"'>
        y
       </a>
       <a alt='Teachers beginning with "Z"' href="/teachers/directory/z" title='Teachers beginning with "Z"'>
        z
       </a>
      </div>
     </div>
     <div class="row footer_countries_list">
      <div class="col-xs-10 col-xs-offset-1 col-sm-12 col-sm-offset-0">
       RateMyTeachers International:
       <a alt="United States" class="country" href="https://www.ratemyteachers.com" title="United States">
        United States
       </a>
       <a alt="Canada" class="country" href="https://ca.ratemyteachers.com" title="Canada">
        Canada
       </a>
       <a alt="United Kingdom" class="country" href="https://uk.ratemyteachers.com" title="United Kingdom">
        United Kingdom
       </a>
       <a alt="Australia" class="country" href="https://au.ratemyteachers.com" title="Australia">
        Australia
       </a>
       <a alt="New Zealand" class="country" href="https://nz.ratemyteachers.com" title="New Zealand">
        New Zealand
       </a>
       <a alt="Ireland" class="country" href="https://ie.ratemyteachers.com" title="Ireland">
        Ireland
       </a>
      </div>
     </div>
    </div>
   </section>
   <section class="container-fluid" id="footer">
    <div class="container">
     <div class="row footer_links">
      <div class="col-xs-10 col-xs-offset-1 col-sm-12 col-sm-offset-0">
       <h3 class="hidden-sm hidden-md hidden-lg">
        Quick Links
       </h3>
       <ul>
        <li>
         <a alt="RateMyTeachers Frequently Asked Questions" href="/faq" title="RateMyTeachers Frequently Asked Questions">
          FAQ
         </a>
        </li>
        <li>
         <a data-backdrop="static" data-keyboard="" data-remote="/contact/new" data-target="#modal" data-toggle="modal" href="javascript:void(0);" rel="nofollow" title="Contact RateMyTeachers">
          Contact
         </a>
        </li>
        <li>
         <a href="/terms" title="RateMyTeachers Terms of Use">
          Terms of Use
         </a>
        </li>
        <li>
         <a alt="RateMyTeachers Privacy Policy" href="/privacy" title="RateMyTeachers Privacy Policy">
          Privacy Policy
         </a>
        </li>
        <li>
         <a href="/site-guidelines" title="RateMyTeachers Site Guidelines">
          Site Guidelines
         </a>
        </li>
        <li>
         <a href="/copyright" title="RateMyTeachers Copyright Compliance">
          Copyright Compliance
         </a>
        </li>
       </ul>
      </div>
     </div>
     <div class="row copyright">
      Copyright 2001-2018 RateMyTeachers.com. All Rights Reserved.
     </div>
    </div>
   </section>
   <div aria-hidden="true" class="modal fade" id="modal" role="dialog" style="width: auto;" tabindex="-1">
    <div class="modal-dialog">
     <div class="modal-content">
     </div>
    </div>
   </div>
   <div aria-hidden="true" class="modal fade" id="modal_rating" role="dialog" style="width: auto;" tabindex="-1">
    <div class="modal-dialog">
     <div class="modal-content">
     </div>
    </div>
   </div>
   <div id="loading-indicator" style="display: none;">
    <div>
     Please wait...
     <br/>
     <img alt="Ajax loader" src="/assets/ajax-loader-e483da860d5177651d2a88eda6a66b00.gif"/>
    </div>
   </div>
   <div class="amp_ad_unit amp_ad_unit_template" style="display: none;">
    <a class="amp_clickurl amp_no_text" href="javascript:void(0);" rel="nofollow" target="_blank">
     <span class="amp_title">
     </span>
     <span class="amp_extension_merchant_rating" style="display: none;">
      <span class="amp_extension_merchant_rating_rating" data-star-width="18">
       <div class="rateit star-rating rateit-exclude" title="">
        <div class="rateit-range" style="width: 90px; height: 15px;">
         <div class="rateit-preset rateit-selected" style="height: 15px; width: 0.000px;">
         </div>
        </div>
       </div>
      </span>
     </span>
     <span class="amp_description">
     </span>
     <span class="amp_displayurl">
     </span>
     <img class="amp_impressionurl" style="height: 1px; width: 1px;"/>
    </a>
    <span class="row amp_extension_site_links">
    </span>
    <span class="arrow">
     <span class="aux">
     </span>
    </span>
    <span class="amp_site_link_template" style="display: none;">
     <a class="col-xs-6 amp_extension_site_links_link">
      <span class="amp_extension_site_links_text">
      </span>
     </a>
    </span>
   </div>
  </div>
  <script type="text/javascript">
   functionToLoad.push('//ajax.googleapis.com/ajax/libs/jqueryui/1.11.2/jquery-ui.min.js');
  </script>
  <script type="text/javascript">
   functionToLoad.push('/assets/application-b341b3f30de53e073ed952dffffa800f.js');
    functionToLoad.push('/assets/users-816a475ba77b361e679d83227c475c2f.js');
  </script>
  <script type="text/javascript">
   functionToLoad.push(function() {
        // Facebook like
        // (function(d, s, id) {
        //   var js, fjs = d.getElementsByTagName(s)[0];
        //   if (d.getElementById(id)) return;
        //   js = d.createElement(s); js.id = id;
        //   js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&appId=232453153516852&version=v2.0";
        //   fjs.parentNode.insertBefore(js, fjs);
        // }(document, 'script', 'facebook-jssdk'));

        // Google Plus
        // (function() {
        //   var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true;
        //   po.src = 'https://apis.google.com/js/platform.js';
        //   var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);
        // })();

        // Twitter Follow
        // !function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src="//platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");

      });
  </script>
  <script type="text/javascript">
   functionToLoad.push(["https://www.google.com/jsapi", true, [
    function() {
      enrollmentByEthnicity = {};

      totalStudentsHistory = {} ;
      initSchoolStatsPage(true, true, true);

      google.load("visualization", "1", {
        packages:["corechart"],
        callback: function(){
          $('body').trigger('chart-ready');
        }
      });
    }
  ]]);
  </script>
  <script type="text/javascript">
   functionToLoad.push(function() {
    var ratingCount = 53;
    var minStickyRatingCount = 3;

    if (!isMobile && !isMedium && ratingCount > 0) {
      var stickyColumnRight = $(".sticky_container_right .sticky_column");
      var stickyColumnCenter = $(".sticky_container_center .sticky_column");
      var footerHeight = $('#all_footer_wrapper').outerHeight() + 50;
      var stickyOptions = function(getWidthFrom, topSpacing) {
        if (typeof(topSpacing) == 'undefined' || topSpacing === null)
          topSpacing = 10;
        return {topSpacing:topSpacing, getWidthFrom: getWidthFrom, responsiveWidth: true, bottomSpacing: footerHeight};
      }

      // Make center column options sticky when min results quantity
      if (isMobile || ratingCount > minStickyRatingCount - 1) {
        stickyColumnCenter.sticky(stickyOptions('.sticky_container_center', 0));
      }

      stickyColumnRight.sticky(stickyOptions('.sticky_container_right', 0));
    }
  });
  </script>
  <script type="text/javascript">
   // AMP_ADS Bottom
        functionToLoad.push([function() {
          var bottomUrl = 'https://ratemyteachers_contextual.ampfeed.com/xmlamp/feed?deco=1&extn=0%2C2&ip=66.108.83.14&partner=ratemyteachers_contextual&qt=%5B%22college+scholarship+in+New+York%22%5D&results=4&rfr=https%3A%2F%2Fwww.ratemyteachers.com%2Fdavid-towber%2F172358-t&sub1=Desktop&sub2=Teachers&ua=python-requests%2F2.18.4&v=5';
          ampAdRegister('amp_ads_bottom', bottomUrl, "amp_ad_teacher_unit_template");
        }, true]);
  </script>
  <div class="amp_ad_unit amp_ad_teacher_unit_template" style="display: none;">
   <a class="amp_clickurl amp_no_text" href="javascript:void(0);" rel="nofollow" target="_blank">
    <span class="amp_title">
    </span>
    <span class="amp_displayurl">
    </span>
    <span class="amp_extension_merchant_rating" style="display: none;">
     <span class="amp_extension_merchant_rating_rating" data-star-width="18">
      <div class="rateit star-rating rateit-exclude" title="">
       <div class="rateit-range" style="width: 90px; height: 15px;">
        <div class="rateit-preset rateit-selected" style="height: 15px; width: 0.000px;">
        </div>
       </div>
      </div>
     </span>
    </span>
    <span class="amp_description">
    </span>
    <img class="amp_impressionurl" style="height: 1px; width: 1px;"/>
   </a>
   <span class="row amp_extension_site_links">
   </span>
   <span class="arrow">
    <span class="aux">
    </span>
   </span>
   <span class="amp_site_link_template" style="display: none;">
    <a class="col-xs-6 amp_extension_site_links_link">
     <span class="amp_extension_site_links_text">
     </span>
    </a>
   </span>
  </div>
  <script type="text/javascript">
   function initializeMaps() {
      var length = mapFunctionArray.length;
      for (var i = 0; i < length; i++) {
        mapFunctionArray[i]();
      }
    }

    functionToLoad.push(function() {
      // Don't load google maps when no pending maps
      if (typeof(mapFunctionArray) === 'undefined' || mapFunctionArray.length < 1)
        return;

      var googleMapsId = "AIzaSyDQOhmnZnwlz7TM334xnTn4JByjjxEgq1g";

      var script_path = "https://maps.googleapis.com/maps/api/js?key=" + googleMapsId + "&sensor=false&callback=initializeMaps";
      $.getScript(script_path);

    });
  </script>
  <script type="text/javascript">
   functionToLoad.push(function() {
        $('.search_form input[name=q]').on("autocompleteopen", function(e) {
          var input = $(e.target);
          var url = 'https://ratemyteachers_contextual.ampfeed.com/xmlamp/feed?deco=1&extn=0%2C2&ip=66.108.83.14&partner=ratemyteachers_contextual&results=2&rfr=https%3A%2F%2Fwww.ratemyteachers.com%2Fdavid-towber%2F172358-t&sub1=desktop&sub2=searchbox&ua=python-requests%2F2.18.4&v=5';
          var country = 'United States';
          var location = '';
          var keywords = 'college scholarship in ';
          if ($('#state').val() !== '') {
            location = $("#state option:selected").text();
            location = location.split('-')[0];
            //keywords = 'online colleges in ';
          } else {
            location = country;
            //keywords = 'online colleges in ';
          }
          url += '&qt=["' + encodeURIComponent(keywords + location) + '"]';
          ampAdRegister('amp_ads_autocomplete', url);
        });
      });
  </script>
  <script>
   window.addEventListener('load', function(){
      console.info("[PERF] DomContentLoaded: " + ((new Date()).getTime() - window.beginTimeTrack));
    });

    window.addEventListener('load', function(){
      console.info("[PERF] Load: " + ((new Date()).getTime() - window.beginTimeTrack));
    });
  </script>
  <script type="text/javascript">
   (function() {
      // Load script from url
      var loadScript = function(url, callback) {
        var script = document.createElement("script");
        script.type = "text/javascript";

        // Add on load callback event
        if (callback !== null) {
          if (script.readyState){ //IE
            script.onreadystatechange = function(){
              if (script.readyState == "loaded" || script.readyState == "complete"){
                script.onreadystatechange = null;
                callback();
              }
            };
          } else { //Others
            // Execute callback even when an error happen
            script.onerror = function(e){
              try {
                console.error("An error happen when loading '" + err.target.src + "' script.");
              } catch(err) {} finally {
                callback();
              }
            };
            script.onload = function(){ callback(); };
          }
        }

        // Load the script
        script.src = url;
        document.body.appendChild(script);
      };

      // Load scripts in a sequence instead parallel
      // to make sure frameworks load correctly
      function sequence(index, max, source) {
        if (index < max) {
          var data = functionToLoad.extractElementData(source[index]);

          if (typeof data.element === 'string') {
            if (data.async) {
              // Async script
              loadScript(data.element, function() {
                if (data.subElements.length > 0) {
                  sequence(0, data.subElements.length, data.subElements);
                }
              });
              sequence(index + 1, max, source);
            } else {
              // Sync scripts
              loadScript(data.element, function() {
                if (data.subElements.length > 0) {
                  sequence(0, data.subElements.length, data.subElements);
                }
                sequence(index + 1, max, source);
              });
            }
          } else {
            // Execute callback even when an error happen on the function
            try {
              if (data.async) {
                // Async script
                setTimeout(function() { data.element(); }, 1);
              } else {
                // Sync script
                data.element();
              }
            } catch(err) {
              console.error(err);
            } finally {
              sequence(index + 1, max, source);
            }
          }
        }
      }

      // Load all javascript in a sequence
      var loadDeferredJs = function() {
        sequence(0, functionToLoad.length, functionToLoad);
      };

      // Execute all lazy javascripts after DOM load
      var raf = requestAnimationFrame || mozRequestAnimationFrame ||
          webkitRequestAnimationFrame || msRequestAnimationFrame;
      if (raf) raf(function() { window.setTimeout(loadDeferredJs, 0); });
      else window.addEventListener('load', loadDeferredJs);
    })();
  </script>
 </body>
</html>




# recipes = results_page.find_all('article', class_="recipe-content-card")





# all_a_tags
[<a alt="United States" class="country active" href="https://www.ratemyteachers.com" title="United States">United States</a>,
 <a alt="Canada" class="country " href="https://ca.ratemyteachers.com" title="Canada">Canada</a>,
 <a alt="United Kingdom" class="country " href="https://uk.ratemyteachers.com" title="United Kingdom">United Kingdom</a>,
 <a alt="Australia" class="country " href="https://au.ratemyteachers.com" title="Australia">Australia</a>,
 <a alt="New Zealand" class="country " href="https://nz.ratemyteachers.com" title="New Zealand">New Zealand</a>,
 <a alt="Ireland" class="country " href="https://ie.ratemyteachers.com" title="Ireland">Ireland</a>,
 <a alt="Go to RateMyTeachers Home" href="/" id="rate_my_teachers_logo" title="Go to RateMyTeachers Home"></a>,
 <a href="javascript:void(0);" rel="nofollow">
 <i class="fa fa-bars"></i>
 </a>,
 <a href="/" title="Go to RateMyTeachers Home">United States</a>,
 <a alt="Go to Schools in New York" href="/new-york" title="Go to Schools in New York">New York</a>,
 <a alt="Go to Schools in New York" href="/new-york/new-york" title="Go to Schools in New York">New York</a>,
 <a alt="View Hunter College High School's Teachers" href="/hunter-college-high-school/25767-s" title="View Hunter College High School's Teachers">Hunter College High School</a>,
 <a class="new_teacher_trigger" data-backdrop="static" data-keyboard="" data-remote="/teachers/new?sid=25767" data-school="Hunter College High School" data-sender-name="School page breadcrumb" data-target="#modal" data-toggle="modal" href="javascript:void(0);" rel="nofollow" title="Add My Teacher">Add My Teacher</a>,
 <a class="new_school_rating_trigger" data-backdrop="static" data-keyboard="" data-remote="/school_ratings/new?sid=25767" data-school="Hunter College High School" data-sender-name="School page breadcrumb" data-target="#modal_rating" data-toggle="modal" href="javascript:void(0);" rel="nofollow" title="Rate My School">Rate My School</a>,
 <a href="https://www.ratemyteachers.com/new-york" itemprop="url">
 <span itemprop="title">New York</span>
 </a>,
 <a href="https://www.ratemyteachers.com/new-york/new-york" itemprop="url">
 <span itemprop="title">New York</span>
 </a>,
 <a class="edit school_correction_trigger" data-backdrop="static" data-keyboard="" data-remote="/schools/correction?sid=25767" data-school="Hunter College High School" data-sender-name="School page Main" data-target="#modal" data-toggle="modal" href="javascript:void(0);" rel="nofollow" remote="" title="Submit a Correction">
 Edit
 </a>,
 <a href="/hunter-college-high-school/25767-s/stats" target="_blank">
 Learn More
 </a>,
 <a class="new_school_rating_trigger" data-backdrop="static" data-keyboard="" data-remote="/school_ratings/new?sid=25767" data-sender-name="School page Main" data-target="#modal_rating" data-teacher="Hunter College High School" data-toggle="modal" href="javascript:void(0);" rel="nofollow" remote="" title="Submit Rating for Hunter College High School">
 <i class="fa fa-institution"></i>
 <span class="value">Rate Hunter College High School</span>
 </a>,
 <a href="https://www.google.com/maps/search/71%20E%2094%20St%2C%20New%20York%2C%20New%20York%2010128%2C%20New%20York%2C%20New%20York%2C%2010128%2C%20United%20States" target="_blank" title="71 E 94 St, New York, New York 10128">
 <i class="fa fa-map-marker"></i>
 <span class="value">71 E 94 St, New York, New York 10128</span>
 </a>,
 <a class="school_phone_trigger" data-phone="718-349-4000" href="javascript:void(0);">
 <i class="fa fa-phone"></i>
 <span itemprop="telephone">718-349-4000</span>
 </a>,
 <a href="https://www.hunterschools.org/hs" rel="nofollow" target="_blank" title="https://www.hunterschools.org/hs">
 <i class="fa fa-globe"></i>
 <span itemprop="url">https://www.hunterschools.org/hs</span>
 </a>,
 <a href="https://www.ratemyteachers.com/hunter-college-high-school/25767-s" title="View Hunter College High School's Teachers">
 Faculty:
 218
 Teachers
 </a>,
 <a href="https://www.ratemyteachers.com/hunter-college-high-school/25767-s/school-reviews" title="View Hunter College High School's Reviews">
 Hunter College High School
 Reviews
 </a>,
 <a class="col-xs-4 new_admin_request_trigger apply_admin" data-remote="/admin/new?sid=25767" data-school="Hunter College High School" data-sender="School page Mobile Search Form" data-target="#modal" data-toggle="modal" href="javascript:void(0);" rel="nofollow" title="Become Hunter College High School's Moderator">
 <i class="fa fa-user-plus"></i>
 <span>Become a Moderator!</span>
 </a>,
 <a class="col-xs-4 new_school_rating_trigger school_review" data-backdrop="static" data-keyboard="" data-remote="/school_ratings/new?sid=25767" data-sender-name="School page Search bar" data-target="#modal_rating" data-teacher="Hunter College High School" data-toggle="modal" href="javascript:void(0);" rel="nofollow" remote="" title="Submit Rating for Hunter College High School">
 <i class="fa fa-institution"></i>
 <span>Write a School Review</span>
 </a>,
 <a class="col-xs-4 new_teacher_trigger add_teacher" data-backdrop="static" data-keyboard="" data-remote="/teachers/new?sid=25767" data-school="Hunter College High School" data-sender-name="School page Mobile Search Form" data-target="#modal" data-toggle="modal" href="javascript:void(0);" rel="nofollow" title="Add My Teacher to Hunter College High School">
 <i class="fa fa-user-plus"></i>
 <span>Add Teacher</span>
 </a>,
 
 <a alt="View David Towber's Ratings" class="name" href="/david-towber/172358-t" target="_blank" title="View David Towber's Ratings">
 David Towber
 </a>,
 <a href="/hunter-college-high-school/25767-s/visual-arts" title="View Hunter College High School's Visual Arts Teachers">Visual Arts</a>,
 <a alt="View David Towber's Ratings" class="btn view_more" href="/david-towber/172358-t" title="View David Towber's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/david-towber/172358-t"></a>,
 

 <a alt="View Drew Adams' Ratings" class="name" href="/drew-adams/1078417-t" target="_blank" title="View Drew Adams' Ratings">
 Drew Adams
 </a>,
 <a href="/hunter-college-high-school/25767-s/physical-education" title="View Hunter College High School's Physical Education Teachers">Physical Education</a>,
 <a alt="View Drew Adams' Ratings" class="btn view_more" href="/drew-adams/1078417-t" title="View Drew Adams' Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/drew-adams/1078417-t"></a>,


 <a alt="View Tom Scott's Ratings" class="name" href="/tom-scott/225880-t" target="_blank" title="View Tom Scott's Ratings">
 Tom Scott
 </a>,
 <a href="/hunter-college-high-school/25767-s/science" title="View Hunter College High School's Science Teachers">Science</a>,
 <a alt="View Tom Scott's Ratings" class="btn view_more" href="/tom-scott/225880-t" title="View Tom Scott's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,

 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/tom-scott/225880-t"></a>,
 <a alt="View Micheline Beaudry's Ratings" class="name" href="/micheline-beaudry/239022-t" target="_blank" title="View Micheline Beaudry's Ratings">
 Micheline Beaudry
 </a>,
 <a href="/hunter-college-high-school/25767-s/music" title="View Hunter College High School's Music Teachers">Music</a>,
 <a alt="View Micheline Beaudry's Ratings" class="btn view_more" href="/micheline-beaudry/239022-t" title="View Micheline Beaudry's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/micheline-beaudry/239022-t"></a>,
 <a alt="View Peter Melman's Ratings" class="name" href="/peter-melman/1747652-t" target="_blank" title="View Peter Melman's Ratings">
 Peter Melman
 </a>,
 <a href="/hunter-college-high-school/25767-s/english" title="View Hunter College High School's English Teachers">English</a>,
 <a alt="View Peter Melman's Ratings" class="btn view_more" href="/peter-melman/1747652-t" title="View Peter Melman's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/peter-melman/1747652-t"></a>,
 <a alt="View Ben Morgenroth's Ratings" class="name" href="/ben-morgenroth/3983117-t" target="_blank" title="View Ben Morgenroth's Ratings">
 Ben Morgenroth
 </a>,
 <a href="/hunter-college-high-school/25767-s/math" title="View Hunter College High School's Math Teachers">Math</a>,
 <a alt="View Ben Morgenroth's Ratings" class="btn view_more" href="/ben-morgenroth/3983117-t" title="View Ben Morgenroth's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/ben-morgenroth/3983117-t"></a>,
 <a alt="View Eliza Kuberska's Ratings" class="name" href="/eliza-kuberska/193595-t" target="_blank" title="View Eliza Kuberska's Ratings">
 Eliza Kuberska
 </a>,
 <a href="/hunter-college-high-school/25767-s/math" title="View Hunter College High School's Math Teachers">Math</a>,
 <a alt="View Eliza Kuberska's Ratings" class="btn view_more" href="/eliza-kuberska/193595-t" title="View Eliza Kuberska's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/eliza-kuberska/193595-t"></a>,
 <a alt="View Bradley Scalise's Ratings" class="name" href="/bradley-scalise/7918595-t" target="_blank" title="View Bradley Scalise's Ratings">
 Bradley Scalise
 </a>,
 <a href="/hunter-college-high-school/25767-s/science" title="View Hunter College High School's Science Teachers">Science</a>,
 <a alt="View Bradley Scalise's Ratings" class="btn view_more" href="/bradley-scalise/7918595-t" title="View Bradley Scalise's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/bradley-scalise/7918595-t"></a>,
 <a alt="View Larry Ling's Ratings" class="name" href="/larry-ling/237643-t" target="_blank" title="View Larry Ling's Ratings">
 Larry Ling
 </a>,
 <a href="/hunter-college-high-school/25767-s/languages" title="View Hunter College High School's Languages Teachers">Languages</a>,
 <a alt="View Larry Ling's Ratings" class="btn view_more" href="/larry-ling/237643-t" title="View Larry Ling's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/larry-ling/237643-t"></a>,
 <a alt="View Richard Fulco's Ratings" class="name" href="/richard-fulco/1104609-t" target="_blank" title="View Richard Fulco's Ratings">
 Richard Fulco
 </a>,
 <a href="/hunter-college-high-school/25767-s/english" title="View Hunter College High School's English Teachers">English</a>,
 <a alt="View Richard Fulco's Ratings" class="btn view_more" href="/richard-fulco/1104609-t" title="View Richard Fulco's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/richard-fulco/1104609-t"></a>,
 <a alt="View Elizabeth Fox's Ratings" class="name" href="/elizabeth-fox/231055-t" target="_blank" title="View Elizabeth Fox's Ratings">
 Elizabeth Fox
 </a>,
 <a href="/hunter-college-high-school/25767-s/physical-education" title="View Hunter College High School's Physical Education Teachers">Physical Education</a>,
 <a alt="View Elizabeth Fox's Ratings" class="btn view_more" href="/elizabeth-fox/231055-t" title="View Elizabeth Fox's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/elizabeth-fox/231055-t"></a>,
 <a alt="View Tony Fisher's Ratings" class="name" href="/tony-fisher/1681402-t" target="_blank" title="View Tony Fisher's Ratings">
 Tony Fisher
 </a>,
 <a href="/hunter-college-high-school/25767-s/math" title="View Hunter College High School's Math Teachers">Math</a>,
 <a alt="View Tony Fisher's Ratings" class="btn view_more" href="/tony-fisher/1681402-t" title="View Tony Fisher's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/tony-fisher/1681402-t"></a>,
 <a alt="View Steve Borowka's Ratings" class="name" href="/steve-borowka/1655713-t" target="_blank" title="View Steve Borowka's Ratings">
 Steve Borowka
 </a>,
 <a href="/hunter-college-high-school/25767-s/performing-arts" title="View Hunter College High School's Performing Arts Teachers">Performing Arts</a>,
 <a alt="View Steve Borowka's Ratings" class="btn view_more" href="/steve-borowka/1655713-t" title="View Steve Borowka's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/steve-borowka/1655713-t"></a>,
 <a alt="View Margaret Sturiano's Ratings" class="name" href="/margaret-sturiano/1371640-t" target="_blank" title="View Margaret Sturiano's Ratings">
 Margaret Sturiano
 </a>,
 <a href="/hunter-college-high-school/25767-s/performing-arts" title="View Hunter College High School's Performing Arts Teachers">Performing Arts</a>,
 <a alt="View Margaret Sturiano's Ratings" class="btn view_more" href="/margaret-sturiano/1371640-t" title="View Margaret Sturiano's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/margaret-sturiano/1371640-t"></a>,
 <a alt="View Sylvia Schaindlin's Ratings" class="name" href="/sylvia-schaindlin/242184-t" target="_blank" title="View Sylvia Schaindlin's Ratings">
 Sylvia Schaindlin
 </a>,
 <a href="/hunter-college-high-school/25767-s/math" title="View Hunter College High School's Math Teachers">Math</a>,
 <a alt="View Sylvia Schaindlin's Ratings" class="btn view_more" href="/sylvia-schaindlin/242184-t" title="View Sylvia Schaindlin's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/sylvia-schaindlin/242184-t"></a>,
 <a alt="View Luke Batson's Ratings" class="name" href="/luke-batson/1352298-t" target="_blank" title="View Luke Batson's Ratings">
 Luke Batson
 </a>,
 <a href="/hunter-college-high-school/25767-s/music" title="View Hunter College High School's Music Teachers">Music</a>,
 <a alt="View Luke Batson's Ratings" class="btn view_more" href="/luke-batson/1352298-t" title="View Luke Batson's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/luke-batson/1352298-t"></a>,
 <a alt="View Linda Aboody's Ratings" class="name" href="/linda-aboody/193569-t" target="_blank" title="View Linda Aboody's Ratings">
 Linda Aboody
 </a>,
 <a href="/hunter-college-high-school/25767-s/math" title="View Hunter College High School's Math Teachers">Math</a>,
 <a alt="View Linda Aboody's Ratings" class="btn view_more" href="/linda-aboody/193569-t" title="View Linda Aboody's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/linda-aboody/193569-t"></a>,
 <a alt="View Lourdie Castillo's Ratings" class="name" href="/lourdie-castillo/7911689-t" target="_blank" title="View Lourdie Castillo's Ratings">
 Lourdie Castillo
 </a>,
 <a href="/hunter-college-high-school/25767-s/chemistry" title="View Hunter College High School's Chemistry Teachers">Chemistry</a>,
 <a alt="View Lourdie Castillo's Ratings" class="btn view_more" href="/lourdie-castillo/7911689-t" title="View Lourdie Castillo's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/lourdie-castillo/7911689-t"></a>,
 <a alt="View Gregory Boyle's Ratings" class="name" href="/gregory-boyle/248077-t" target="_blank" title="View Gregory Boyle's Ratings">
 Gregory Boyle
 </a>,
 <a href="/hunter-college-high-school/25767-s/social-studies" title="View Hunter College High School's Social Studies Teachers">Social Studies</a>,
 <a alt="View Gregory Boyle's Ratings" class="btn view_more" href="/gregory-boyle/248077-t" title="View Gregory Boyle's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/gregory-boyle/248077-t"></a>,
 <a alt="View Caitlin Samuel's Ratings" class="name" href="/caitlin-samuel/3993811-t" target="_blank" title="View Caitlin Samuel's Ratings">
 Caitlin Samuel
 </a>,
 <a href="/hunter-college-high-school/25767-s/science" title="View Hunter College High School's Science Teachers">Science</a>,
 <a alt="View Caitlin Samuel's Ratings" class="btn view_more" href="/caitlin-samuel/3993811-t" title="View Caitlin Samuel's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/caitlin-samuel/3993811-t"></a>,
 <a alt="View Kasumi Parker's Ratings" class="name" href="/kasumi-parker/2146288-t" target="_blank" title="View Kasumi Parker's Ratings">
 Kasumi Parker
 </a>,
 <a href="/hunter-college-high-school/25767-s/english" title="View Hunter College High School's English Teachers">English</a>,
 <a alt="View Kasumi Parker's Ratings" class="btn view_more" href="/kasumi-parker/2146288-t" title="View Kasumi Parker's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/kasumi-parker/2146288-t"></a>,
 <a alt="View Michael Keleher's Ratings" class="name" href="/michael-keleher/7911691-t" target="_blank" title="View Michael Keleher's Ratings">
 Michael Keleher
 </a>,
 <a href="/hunter-college-high-school/25767-s/french" title="View Hunter College High School's French Teachers">French</a>,
 <a alt="View Michael Keleher's Ratings" class="btn view_more" href="/michael-keleher/7911691-t" title="View Michael Keleher's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/michael-keleher/7911691-t"></a>,
 <a alt="View Audrey Maurer's Ratings" class="name" href="/audrey-maurer/2493647-t" target="_blank" title="View Audrey Maurer's Ratings">
 Audrey Maurer
 </a>,
 <a href="/hunter-college-high-school/25767-s/french" title="View Hunter College High School's French Teachers">French</a>,
 <a alt="View Audrey Maurer's Ratings" class="btn view_more" href="/audrey-maurer/2493647-t" title="View Audrey Maurer's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/audrey-maurer/2493647-t"></a>,
 <a alt="View Olivia Byun's Ratings" class="name" href="/olivia-byun/8057509-t" target="_blank" title="View Olivia Byun's Ratings">
 Olivia Byun
 </a>,
 <a href="/hunter-college-high-school/25767-s/drafting" title="View Hunter College High School's Drafting Teachers">Drafting</a>,
 <a alt="View Olivia Byun's Ratings" class="btn view_more" href="/olivia-byun/8057509-t" title="View Olivia Byun's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/olivia-byun/8057509-t"></a>,
 <a alt="View Daniel Sangermano's Ratings" class="name" href="/daniel-sangermano/682137-t" target="_blank" title="View Daniel Sangermano's Ratings">
 Daniel Sangermano
 </a>,
 <a href="/hunter-college-high-school/25767-s/fine-arts" title="View Hunter College High School's Fine Arts Teachers">Fine Arts</a>,
 <a alt="View Daniel Sangermano's Ratings" class="btn view_more" href="/daniel-sangermano/682137-t" title="View Daniel Sangermano's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/daniel-sangermano/682137-t"></a>,
 <a alt="View Carol Samuel's Ratings" class="name" href="/carol-samuel/1376051-t" target="_blank" title="View Carol Samuel's Ratings">
 Carol Samuel
 </a>,
 <a href="/hunter-college-high-school/25767-s/substitute-teacher" title="View Hunter College High School's Substitute Teacher Teachers">Substitute Teacher</a>,
 <a alt="View Carol Samuel's Ratings" class="btn view_more" href="/carol-samuel/1376051-t" title="View Carol Samuel's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/carol-samuel/1376051-t"></a>,
 <a alt="View Claire Mazzola's Ratings" class="name" href="/claire-mazzola/193564-t" target="_blank" title="View Claire Mazzola's Ratings">
 Claire Mazzola
 </a>,
 <a href="/hunter-college-high-school/25767-s/languages" title="View Hunter College High School's Languages Teachers">Languages</a>,
 <a alt="View Claire Mazzola's Ratings" class="btn view_more" href="/claire-mazzola/193564-t" title="View Claire Mazzola's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/claire-mazzola/193564-t"></a>,
 <a alt="View Satinder Jawanda's Ratings" class="name" href="/satinder-jawanda/826502-t" target="_blank" title="View Satinder Jawanda's Ratings">
 Satinder Jawanda
 </a>,
 <a href="/hunter-college-high-school/25767-s/social-studies" title="View Hunter College High School's Social Studies Teachers">Social Studies</a>,
 <a alt="View Satinder Jawanda's Ratings" class="btn view_more" href="/satinder-jawanda/826502-t" title="View Satinder Jawanda's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/satinder-jawanda/826502-t"></a>,
 <a alt="View Nikki Weinstein's Ratings" class="name" href="/nikki-weinstein/1652812-t" target="_blank" title="View Nikki Weinstein's Ratings">
 Nikki Weinstein
 </a>,
 <a href="/hunter-college-high-school/25767-s/english" title="View Hunter College High School's English Teachers">English</a>,
 <a alt="View Nikki Weinstein's Ratings" class="btn view_more" href="/nikki-weinstein/1652812-t" title="View Nikki Weinstein's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/nikki-weinstein/1652812-t"></a>,
 <a alt="View Stacy Goldstein's Ratings" class="name" href="/stacy-goldstein/1643756-t" target="_blank" title="View Stacy Goldstein's Ratings">
 Stacy Goldstein
 </a>,
 <a href="/hunter-college-high-school/25767-s/biology" title="View Hunter College High School's Biology Teachers">Biology</a>,
 <a alt="View Stacy Goldstein's Ratings" class="btn view_more" href="/stacy-goldstein/1643756-t" title="View Stacy Goldstein's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/stacy-goldstein/1643756-t"></a>,
 <a alt="View Amelia Betancourt's Ratings" class="name" href="/amelia-betancourt/1643770-t" target="_blank" title="View Amelia Betancourt's Ratings">
 Amelia Betancourt
 </a>,
 <a href="/hunter-college-high-school/25767-s/languages" title="View Hunter College High School's Languages Teachers">Languages</a>,
 <a alt="View Amelia Betancourt's Ratings" class="btn view_more" href="/amelia-betancourt/1643770-t" title="View Amelia Betancourt's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/amelia-betancourt/1643770-t"></a>,
 <a alt="View Michael Stratechuk's Ratings" class="name" href="/michael-stratechuk/234440-t" target="_blank" title="View Michael Stratechuk's Ratings">
 Michael Stratechuk
 </a>,
 <a href="/hunter-college-high-school/25767-s/music" title="View Hunter College High School's Music Teachers">Music</a>,
 <a alt="View Michael Stratechuk's Ratings" class="btn view_more" href="/michael-stratechuk/234440-t" title="View Michael Stratechuk's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/michael-stratechuk/234440-t"></a>,
 <a alt="View Roni Mistriel's Ratings" class="name" href="/roni-mistriel/242967-t" target="_blank" title="View Roni Mistriel's Ratings">
 Roni Mistriel
 </a>,
 <a href="/hunter-college-high-school/25767-s/physical-education" title="View Hunter College High School's Physical Education Teachers">Physical Education</a>,
 <a alt="View Roni Mistriel's Ratings" class="btn view_more" href="/roni-mistriel/242967-t" title="View Roni Mistriel's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/roni-mistriel/242967-t"></a>,
 <a alt="View Brian Park's Ratings" class="name" href="/brian-park/1683905-t" target="_blank" title="View Brian Park's Ratings">
 Brian Park
 </a>,
 <a href="/hunter-college-high-school/25767-s/science" title="View Hunter College High School's Science Teachers">Science</a>,
 <a alt="View Brian Park's Ratings" class="btn view_more" href="/brian-park/1683905-t" title="View Brian Park's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/brian-park/1683905-t"></a>,
 <a alt="View Kip Zegers' Ratings" class="name" href="/kip-zegers/246707-t" target="_blank" title="View Kip Zegers' Ratings">
 Kip Zegers
 </a>,
 <a href="/hunter-college-high-school/25767-s/english" title="View Hunter College High School's English Teachers">English</a>,
 <a alt="View Kip Zegers' Ratings" class="btn view_more" href="/kip-zegers/246707-t" title="View Kip Zegers' Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/kip-zegers/246707-t"></a>,
 <a alt="View Melissa Chapnick's Ratings" class="name" href="/melissa-chapnick/1353338-t" target="_blank" title="View Melissa Chapnick's Ratings">
 Melissa Chapnick
 </a>,
 <a href="/hunter-college-high-school/25767-s/social-studies" title="View Hunter College High School's Social Studies Teachers">Social Studies</a>,
 <a alt="View Melissa Chapnick's Ratings" class="btn view_more" href="/melissa-chapnick/1353338-t" title="View Melissa Chapnick's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/melissa-chapnick/1353338-t"></a>,
 <a alt="View Sarah Fogelman's Ratings" class="name" href="/sarah-fogelman/486096-t" target="_blank" title="View Sarah Fogelman's Ratings">
 Sarah Fogelman
 </a>,
 <a href="/hunter-college-high-school/25767-s/science" title="View Hunter College High School's Science Teachers">Science</a>,
 <a alt="View Sarah Fogelman's Ratings" class="btn view_more" href="/sarah-fogelman/486096-t" title="View Sarah Fogelman's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/sarah-fogelman/486096-t"></a>,
 <a alt="View Jana Lucash's Ratings" class="name" href="/jana-lucash/271302-t" target="_blank" title="View Jana Lucash's Ratings">
 Jana Lucash
 </a>,
 <a href="/hunter-college-high-school/25767-s/social-studies" title="View Hunter College High School's Social Studies Teachers">Social Studies</a>,
 <a alt="View Jana Lucash's Ratings" class="btn view_more" href="/jana-lucash/271302-t" title="View Jana Lucash's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/jana-lucash/271302-t"></a>,
 <a alt="View Sheila Garcia's Ratings" class="name" href="/sheila-garcia/312565-t" target="_blank" title="View Sheila Garcia's Ratings">
 Sheila Garcia
 </a>,
 <a href="/hunter-college-high-school/25767-s/counselor" title="View Hunter College High School's Counselor Teachers">Counselor</a>,
 <a alt="View Sheila Garcia's Ratings" class="btn view_more" href="/sheila-garcia/312565-t" title="View Sheila Garcia's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/sheila-garcia/312565-t"></a>,
 <a alt="View Rembert Herbert's Ratings" class="name" href="/rembert-herbert/211443-t" target="_blank" title="View Rembert Herbert's Ratings">
 Rembert Herbert
 </a>,
 <a href="/hunter-college-high-school/25767-s/english" title="View Hunter College High School's English Teachers">English</a>,
 <a alt="View Rembert Herbert's Ratings" class="btn view_more" href="/rembert-herbert/211443-t" title="View Rembert Herbert's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/rembert-herbert/211443-t"></a>,
 <a alt="View Martha Curtis' Ratings" class="name" href="/martha-curtis/234435-t" target="_blank" title="View Martha Curtis' Ratings">
 Martha Curtis
 </a>,
 <a href="/hunter-college-high-school/25767-s/social-studies" title="View Hunter College High School's Social Studies Teachers">Social Studies</a>,
 <a alt="View Martha Curtis' Ratings" class="btn view_more" href="/martha-curtis/234435-t" title="View Martha Curtis' Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/martha-curtis/234435-t"></a>,
 <a alt="View Lillian Drvostep's Ratings" class="name" href="/lillian-drvostep/229540-t" target="_blank" title="View Lillian Drvostep's Ratings">
 Lillian Drvostep
 </a>,
 <a href="/hunter-college-high-school/25767-s/health" title="View Hunter College High School's Health Teachers">Health</a>,
 <a alt="View Lillian Drvostep's Ratings" class="btn view_more" href="/lillian-drvostep/229540-t" title="View Lillian Drvostep's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/lillian-drvostep/229540-t"></a>,
 <a alt="View Constance Rich's Ratings" class="name" href="/constance-rich/193686-t" target="_blank" title="View Constance Rich's Ratings">
 Constance Rich
 </a>,
 <a href="/hunter-college-high-school/25767-s/visual-arts" title="View Hunter College High School's Visual Arts Teachers">Visual Arts</a>,
 <a alt="View Constance Rich's Ratings" class="btn view_more" href="/constance-rich/193686-t" title="View Constance Rich's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/constance-rich/193686-t"></a>,
 <a alt="View Irving Kagan's Ratings" class="name" href="/irving-kagan/234414-t" target="_blank" title="View Irving Kagan's Ratings">
 Irving Kagan
 </a>,
 <a href="/hunter-college-high-school/25767-s/social-studies" title="View Hunter College High School's Social Studies Teachers">Social Studies</a>,
 <a alt="View Irving Kagan's Ratings" class="btn view_more" href="/irving-kagan/234414-t" title="View Irving Kagan's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/irving-kagan/234414-t"></a>,
 <a alt="View Betty Kleinfeld's Ratings" class="name" href="/betty-kleinfeld/323464-t" target="_blank" title="View Betty Kleinfeld's Ratings">
 Betty Kleinfeld
 </a>,
 <a href="/hunter-college-high-school/25767-s/social-studies" title="View Hunter College High School's Social Studies Teachers">Social Studies</a>,
 <a alt="View Betty Kleinfeld's Ratings" class="btn view_more" href="/betty-kleinfeld/323464-t" title="View Betty Kleinfeld's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/betty-kleinfeld/323464-t"></a>,
 <a alt="View David Joffe's Ratings" class="name" href="/david-joffe/1340051-t" target="_blank" title="View David Joffe's Ratings">
 David Joffe
 </a>,
 <a href="/hunter-college-high-school/25767-s/social-studies" title="View Hunter College High School's Social Studies Teachers">Social Studies</a>,
 <a alt="View David Joffe's Ratings" class="btn view_more" href="/david-joffe/1340051-t" title="View David Joffe's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/david-joffe/1340051-t"></a>,
 <a alt="View Rebecca Hollander's Ratings" class="name" href="/rebecca-hollander/234520-t" target="_blank" title="View Rebecca Hollander's Ratings">
 Rebecca Hollander
 </a>,
 <a href="/hunter-college-high-school/25767-s/communications" title="View Hunter College High School's Communications Teachers">Communications</a>,
 <a alt="View Rebecca Hollander's Ratings" class="btn view_more" href="/rebecca-hollander/234520-t" title="View Rebecca Hollander's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/rebecca-hollander/234520-t"></a>,
 <a alt="View Sheila Krilov's Ratings" class="name" href="/sheila-krilov/234397-t" target="_blank" title="View Sheila Krilov's Ratings">
 Sheila Krilov
 </a>,
 <a href="/hunter-college-high-school/25767-s/math" title="View Hunter College High School's Math Teachers">Math</a>,
 <a alt="View Sheila Krilov's Ratings" class="btn view_more" href="/sheila-krilov/234397-t" title="View Sheila Krilov's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/sheila-krilov/234397-t"></a>,
 <a alt="View Bob Gaudenzi's Ratings" class="name" href="/bob-gaudenzi/244030-t" target="_blank" title="View Bob Gaudenzi's Ratings">
 Bob Gaudenzi
 </a>,
 <a href="/hunter-college-high-school/25767-s/physical-education" title="View Hunter College High School's Physical Education Teachers">Physical Education</a>,
 <a alt="View Bob Gaudenzi's Ratings" class="btn view_more" href="/bob-gaudenzi/244030-t" title="View Bob Gaudenzi's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/bob-gaudenzi/244030-t"></a>,
 <a alt="View Christopher Unruh's Ratings" class="name" href="/christopher-unruh/529880-t" target="_blank" title="View Christopher Unruh's Ratings">
 Christopher Unruh
 </a>,
 <a href="/hunter-college-high-school/25767-s/languages" title="View Hunter College High School's Languages Teachers">Languages</a>,
 <a alt="View Christopher Unruh's Ratings" class="btn view_more" href="/christopher-unruh/529880-t" title="View Christopher Unruh's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/christopher-unruh/529880-t"></a>,
 <a alt="View Ray Kaniatyn's Ratings" class="name" href="/ray-kaniatyn/242188-t" target="_blank" title="View Ray Kaniatyn's Ratings">
 Ray Kaniatyn
 </a>,
 <a href="/hunter-college-high-school/25767-s/physical-education" title="View Hunter College High School's Physical Education Teachers">Physical Education</a>,
 <a alt="View Ray Kaniatyn's Ratings" class="btn view_more" href="/ray-kaniatyn/242188-t" title="View Ray Kaniatyn's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/ray-kaniatyn/242188-t"></a>,
 <a alt="View Thomas Keenan's Ratings" class="name" href="/thomas-keenan/478475-t" target="_blank" title="View Thomas Keenan's Ratings">
 Thomas Keenan
 </a>,
 <a href="/hunter-college-high-school/25767-s/science" title="View Hunter College High School's Science Teachers">Science</a>,
 <a alt="View Thomas Keenan's Ratings" class="btn view_more" href="/thomas-keenan/478475-t" title="View Thomas Keenan's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/thomas-keenan/478475-t"></a>,
 <a alt="View Clare Kudera's Ratings" class="name" href="/clare-kudera/232426-t" target="_blank" title="View Clare Kudera's Ratings">
 Clare Kudera
 </a>,
 <a href="/hunter-college-high-school/25767-s/social-studies" title="View Hunter College High School's Social Studies Teachers">Social Studies</a>,
 <a alt="View Clare Kudera's Ratings" class="btn view_more" href="/clare-kudera/232426-t" title="View Clare Kudera's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/clare-kudera/232426-t"></a>,
 <a alt="View Rebecca Ramirez's Ratings" class="name" href="/rebecca-ramirez/1638618-t" target="_blank" title="View Rebecca Ramirez's Ratings">
 Rebecca Ramirez
 </a>,
 <a href="/hunter-college-high-school/25767-s/languages" title="View Hunter College High School's Languages Teachers">Languages</a>,
 <a alt="View Rebecca Ramirez's Ratings" class="btn view_more" href="/rebecca-ramirez/1638618-t" title="View Rebecca Ramirez's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/rebecca-ramirez/1638618-t"></a>,
 <a alt="View Richard Roundy's Ratings" class="name" href="/richard-roundy/224414-t" target="_blank" title="View Richard Roundy's Ratings">
 Richard Roundy
 </a>,
 <a href="/hunter-college-high-school/25767-s/english" title="View Hunter College High School's English Teachers">English</a>,
 <a alt="View Richard Roundy's Ratings" class="btn view_more" href="/richard-roundy/224414-t" title="View Richard Roundy's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/richard-roundy/224414-t"></a>,
 <a alt="View Tara Foley's Ratings" class="name" href="/tara-foley/1714190-t" target="_blank" title="View Tara Foley's Ratings">
 Tara Foley
 </a>,
 <a href="/hunter-college-high-school/25767-s/english" title="View Hunter College High School's English Teachers">English</a>,
 <a alt="View Tara Foley's Ratings" class="btn view_more" href="/tara-foley/1714190-t" title="View Tara Foley's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/tara-foley/1714190-t"></a>,
 <a alt="View Hal Weinstein's Ratings" class="name" href="/hal-weinstein/316663-t" target="_blank" title="View Hal Weinstein's Ratings">
 Hal Weinstein
 </a>,
 <a href="/hunter-college-high-school/25767-s/math" title="View Hunter College High School's Math Teachers">Math</a>,
 <a alt="View Hal Weinstein's Ratings" class="btn view_more" href="/hal-weinstein/316663-t" title="View Hal Weinstein's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/hal-weinstein/316663-t"></a>,
 <a alt="View Rachel Basker's Ratings" class="name" href="/rachel-basker/246734-t" target="_blank" title="View Rachel Basker's Ratings">
 Rachel Basker
 </a>,
 <a href="/hunter-college-high-school/25767-s/science" title="View Hunter College High School's Science Teachers">Science</a>,
 <a alt="View Rachel Basker's Ratings" class="btn view_more" href="/rachel-basker/246734-t" title="View Rachel Basker's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/rachel-basker/246734-t"></a>,
 <a alt="View Christina Moore's Ratings" class="name" href="/christina-moore/1032723-t" target="_blank" title="View Christina Moore's Ratings">
 Christina Moore
 </a>,
 <a href="/hunter-college-high-school/25767-s/math" title="View Hunter College High School's Math Teachers">Math</a>,
 <a alt="View Christina Moore's Ratings" class="btn view_more" href="/christina-moore/1032723-t" title="View Christina Moore's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/christina-moore/1032723-t"></a>,
 <a alt="View Ann Slavin's Ratings" class="name" href="/ann-slavin/242978-t" target="_blank" title="View Ann Slavin's Ratings">
 Ann Slavin
 </a>,
 <a href="/hunter-college-high-school/25767-s/languages" title="View Hunter College High School's Languages Teachers">Languages</a>,
 <a alt="View Ann Slavin's Ratings" class="btn view_more" href="/ann-slavin/242978-t" title="View Ann Slavin's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/ann-slavin/242978-t"></a>,
 <a alt="View Johnson Wong's Ratings" class="name" href="/johnson-wong/1479620-t" target="_blank" title="View Johnson Wong's Ratings">
 Johnson Wong
 </a>,
 <a href="/hunter-college-high-school/25767-s/physical-education" title="View Hunter College High School's Physical Education Teachers">Physical Education</a>,
 <a alt="View Johnson Wong's Ratings" class="btn view_more" href="/johnson-wong/1479620-t" title="View Johnson Wong's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/johnson-wong/1479620-t"></a>,
 <a alt="View Julie Reifer's Ratings" class="name" href="/julie-reifer/239002-t" target="_blank" title="View Julie Reifer's Ratings">
 Julie Reifer
 </a>,
 <a href="/hunter-college-high-school/25767-s/visual-arts" title="View Hunter College High School's Visual Arts Teachers">Visual Arts</a>,
 <a alt="View Julie Reifer's Ratings" class="btn view_more" href="/julie-reifer/239002-t" title="View Julie Reifer's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/julie-reifer/239002-t"></a>,
 <a alt="View Joanne Roque's Ratings" class="name" href="/joanne-roque/246855-t" target="_blank" title="View Joanne Roque's Ratings">
 Joanne Roque
 </a>,
 <a href="/hunter-college-high-school/25767-s/physics" title="View Hunter College High School's Physics Teachers">Physics</a>,
 <a alt="View Joanne Roque's Ratings" class="btn view_more" href="/joanne-roque/246855-t" title="View Joanne Roque's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/joanne-roque/246855-t"></a>,
 <a alt="View Sewell's Ratings" class="name" href="/sewell/1054170-t" target="_blank" title="View Sewell's Ratings">
 Mrs. Sewell
 </a>,
 <a href="/hunter-college-high-school/25767-s/science" title="View Hunter College High School's Science Teachers">Science</a>,
 <a alt="View Sewell's Ratings" class="btn view_more" href="/sewell/1054170-t" title="View Sewell's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/sewell/1054170-t"></a>,
 <a alt="View Jose Diaz's Ratings" class="name" href="/jose-diaz/234507-t" target="_blank" title="View Jose Diaz's Ratings">
 Jose Diaz
 </a>,
 <a href="/hunter-college-high-school/25767-s/languages" title="View Hunter College High School's Languages Teachers">Languages</a>,
 <a alt="View Jose Diaz's Ratings" class="btn view_more" href="/jose-diaz/234507-t" title="View Jose Diaz's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/jose-diaz/234507-t"></a>,
 <a alt="View Melanie Pflaum's Ratings" class="name" href="/melanie-pflaum/1723216-t" target="_blank" title="View Melanie Pflaum's Ratings">
 Melanie Pflaum
 </a>,
 <a href="/hunter-college-high-school/25767-s/math" title="View Hunter College High School's Math Teachers">Math</a>,
 <a alt="View Melanie Pflaum's Ratings" class="btn view_more" href="/melanie-pflaum/1723216-t" title="View Melanie Pflaum's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/melanie-pflaum/1723216-t"></a>,
 <a alt="View Evanthia Basias' Ratings" class="name" href="/evanthia-basias/246866-t" target="_blank" title="View Evanthia Basias' Ratings">
 Evanthia Basias
 </a>,
 <a href="/hunter-college-high-school/25767-s/math" title="View Hunter College High School's Math Teachers">Math</a>,
 <a alt="View Evanthia Basias' Ratings" class="btn view_more" href="/evanthia-basias/246866-t" title="View Evanthia Basias' Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/evanthia-basias/246866-t"></a>,
 <a alt="View Shannon Connors' Ratings" class="name" href="/shannon-connors/1888882-t" target="_blank" title="View Shannon Connors' Ratings">
 Shannon Connors
 </a>,
 <a href="/hunter-college-high-school/25767-s/math" title="View Hunter College High School's Math Teachers">Math</a>,
 <a alt="View Shannon Connors' Ratings" class="btn view_more" href="/shannon-connors/1888882-t" title="View Shannon Connors' Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/shannon-connors/1888882-t"></a>,
 <a alt="View Shawn Crouch's Ratings" class="name" href="/shawn-crouch/240689-t" target="_blank" title="View Shawn Crouch's Ratings">
 Shawn Crouch
 </a>,
 <a href="/hunter-college-high-school/25767-s/music" title="View Hunter College High School's Music Teachers">Music</a>,
 <a alt="View Shawn Crouch's Ratings" class="btn view_more" href="/shawn-crouch/240689-t" title="View Shawn Crouch's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/shawn-crouch/240689-t"></a>,
 <a alt="View Neil Potter's Ratings" class="name" href="/neil-potter/259598-t" target="_blank" title="View Neil Potter's Ratings">
 Neil Potter
 </a>,
 <a href="/hunter-college-high-school/25767-s/physical-education" title="View Hunter College High School's Physical Education Teachers">Physical Education</a>,
 <a alt="View Neil Potter's Ratings" class="btn view_more" href="/neil-potter/259598-t" title="View Neil Potter's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/neil-potter/259598-t"></a>,
 <a alt="View Asumana Randolph's Ratings" class="name" href="/asumana-randolph/284663-t" target="_blank" title="View Asumana Randolph's Ratings">
 Asumana Randolph
 </a>,
 <a href="/hunter-college-high-school/25767-s/science" title="View Hunter College High School's Science Teachers">Science</a>,
 <a alt="View Asumana Randolph's Ratings" class="btn view_more" href="/asumana-randolph/284663-t" title="View Asumana Randolph's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/asumana-randolph/284663-t"></a>,
 <a alt="View Gilana Reiss' Ratings" class="name" href="/gilana-reiss/1895207-t" target="_blank" title="View Gilana Reiss' Ratings">
 Gilana Reiss
 </a>,
 <a href="/hunter-college-high-school/25767-s/chemistry" title="View Hunter College High School's Chemistry Teachers">Chemistry</a>,
 <a alt="View Gilana Reiss' Ratings" class="btn view_more" href="/gilana-reiss/1895207-t" title="View Gilana Reiss' Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/gilana-reiss/1895207-t"></a>,
 <a alt="View Justin Storer's Ratings" class="name" href="/justin-storer/1901835-t" target="_blank" title="View Justin Storer's Ratings">
 Justin Storer
 </a>,
 <a href="/hunter-college-high-school/25767-s/math" title="View Hunter College High School's Math Teachers">Math</a>,
 <a alt="View Justin Storer's Ratings" class="btn view_more" href="/justin-storer/1901835-t" title="View Justin Storer's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/justin-storer/1901835-t"></a>,
 <a alt="View Kimberly Airoldi's Ratings" class="name" href="/kimberly-airoldi/229532-t" target="_blank" title="View Kimberly Airoldi's Ratings">
 Kimberly Airoldi
 </a>,
 <a href="/hunter-college-high-school/25767-s/english" title="View Hunter College High School's English Teachers">English</a>,
 <a alt="View Kimberly Airoldi's Ratings" class="btn view_more" href="/kimberly-airoldi/229532-t" title="View Kimberly Airoldi's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/kimberly-airoldi/229532-t"></a>,
 <a alt="View Sue Monroe's Ratings" class="name" href="/sue-monroe/317823-t" target="_blank" title="View Sue Monroe's Ratings">
 Sue Monroe
 </a>,
 <a href="/hunter-college-high-school/25767-s/science" title="View Hunter College High School's Science Teachers">Science</a>,
 <a alt="View Sue Monroe's Ratings" class="btn view_more" href="/sue-monroe/317823-t" title="View Sue Monroe's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/sue-monroe/317823-t"></a>,
 <a alt="View Emily Mines' Ratings" class="name" href="/emily-mines/7138025-t" target="_blank" title="View Emily Mines' Ratings">
 Emily Mines
 </a>,
 <a href="/hunter-college-high-school/25767-s/math" title="View Hunter College High School's Math Teachers">Math</a>,
 <a alt="View Emily Mines' Ratings" class="btn view_more" href="/emily-mines/7138025-t" title="View Emily Mines' Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/emily-mines/7138025-t"></a>,
 <a alt="View Inalni Sharma's Ratings" class="name" href="/inalni-sharma/2406390-t" target="_blank" title="View Inalni Sharma's Ratings">
 Inalni Sharma
 </a>,
 <a href="/hunter-college-high-school/25767-s/chemistry" title="View Hunter College High School's Chemistry Teachers">Chemistry</a>,
 <a alt="View Inalni Sharma's Ratings" class="btn view_more" href="/inalni-sharma/2406390-t" title="View Inalni Sharma's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/inalni-sharma/2406390-t"></a>,
 <a alt="View Lois Refkin's Ratings" class="name" href="/lois-refkin/242625-t" target="_blank" title="View Lois Refkin's Ratings">
 Lois Refkin
 </a>,
 <a href="/hunter-college-high-school/25767-s/english" title="View Hunter College High School's English Teachers">English</a>,
 <a alt="View Lois Refkin's Ratings" class="btn view_more" href="/lois-refkin/242625-t" title="View Lois Refkin's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/lois-refkin/242625-t"></a>,
 <a alt="View Elaine Schwartz's Ratings" class="name" href="/elaine-schwartz/225812-t" target="_blank" title="View Elaine Schwartz's Ratings">
 Elaine Schwartz
 </a>,
 <a href="/hunter-college-high-school/25767-s/science" title="View Hunter College High School's Science Teachers">Science</a>,
 <a alt="View Elaine Schwartz's Ratings" class="btn view_more" href="/elaine-schwartz/225812-t" title="View Elaine Schwartz's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/elaine-schwartz/225812-t"></a>,
 <a alt="View Steve Young's Ratings" class="name" href="/steve-young/1906178-t" target="_blank" title="View Steve Young's Ratings">
 Steve Young
 </a>,
 <a href="/hunter-college-high-school/25767-s/math-social-studies" title="View Hunter College High School's Math/Social Studies Teachers">Math/Social Studies</a>,
 <a alt="View Steve Young's Ratings" class="btn view_more" href="/steve-young/1906178-t" title="View Steve Young's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/steve-young/1906178-t"></a>,
 <a alt="View Sonya Mosco's Ratings" class="name" href="/sonya-mosco/240827-t" target="_blank" title="View Sonya Mosco's Ratings">
 Sonya Mosco
 </a>,
 <a href="/hunter-college-high-school/25767-s/administration" title="View Hunter College High School's Administration Teachers">Administration</a>,
 <a alt="View Sonya Mosco's Ratings" class="btn view_more" href="/sonya-mosco/240827-t" title="View Sonya Mosco's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/sonya-mosco/240827-t"></a>,
 <a alt="View Yael Wyner's Ratings" class="name" href="/yael-wyner/172356-t" target="_blank" title="View Yael Wyner's Ratings">
 Yael Wyner
 </a>,
 <a href="/hunter-college-high-school/25767-s/science" title="View Hunter College High School's Science Teachers">Science</a>,
 <a alt="View Yael Wyner's Ratings" class="btn view_more" href="/yael-wyner/172356-t" title="View Yael Wyner's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/yael-wyner/172356-t"></a>,
 <a alt="View Giovanna Termini's Ratings" class="name" href="/giovanna-termini/193565-t" target="_blank" title="View Giovanna Termini's Ratings">
 Giovanna Termini
 </a>,
 <a href="/hunter-college-high-school/25767-s/social-studies" title="View Hunter College High School's Social Studies Teachers">Social Studies</a>,
 <a alt="View Giovanna Termini's Ratings" class="btn view_more" href="/giovanna-termini/193565-t" title="View Giovanna Termini's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/giovanna-termini/193565-t"></a>,
 <a alt="View Lori Jean D'Amico's Ratings" class="name" href="/lori-jean-d-amico/172360-t" target="_blank" title="View Lori Jean D'Amico's Ratings">
 Lori Jean D'Amico
 </a>,
 <a href="/hunter-college-high-school/25767-s/english" title="View Hunter College High School's English Teachers">English</a>,
 <a alt="View Lori Jean D'Amico's Ratings" class="btn view_more" href="/lori-jean-d-amico/172360-t" title="View Lori Jean D'Amico's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/lori-jean-d-amico/172360-t"></a>,
 <a alt="View Richard Sasso's Ratings" class="name" href="/richard-sasso/246652-t" target="_blank" title="View Richard Sasso's Ratings">
 Richard Sasso
 </a>,
 <a href="/hunter-college-high-school/25767-s/math" title="View Hunter College High School's Math Teachers">Math</a>,
 <a alt="View Richard Sasso's Ratings" class="btn view_more" href="/richard-sasso/246652-t" title="View Richard Sasso's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/richard-sasso/246652-t"></a>,
 <a alt="View Daniel Mozes' Ratings" class="name" href="/daniel-mozes/1922357-t" target="_blank" title="View Daniel Mozes' Ratings">
 Daniel Mozes
 </a>,
 <a href="/hunter-college-high-school/25767-s/english" title="View Hunter College High School's English Teachers">English</a>,
 <a alt="View Daniel Mozes' Ratings" class="btn view_more" href="/daniel-mozes/1922357-t" title="View Daniel Mozes' Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/daniel-mozes/1922357-t"></a>,
 <a alt="View Michelle Rushforth's Ratings" class="name" href="/michelle-rushforth/1923892-t" target="_blank" title="View Michelle Rushforth's Ratings">
 Michelle Rushforth
 </a>,
 <a href="/hunter-college-high-school/25767-s/health" title="View Hunter College High School's Health Teachers">Health</a>,
 <a alt="View Michelle Rushforth's Ratings" class="btn view_more" href="/michelle-rushforth/1923892-t" title="View Michelle Rushforth's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/michelle-rushforth/1923892-t"></a>,
 <a alt="View Sandra Miley's Ratings" class="name" href="/sandra-miley/262028-t" target="_blank" title="View Sandra Miley's Ratings">
 Sandra Miley
 </a>,
 <a href="/hunter-college-high-school/25767-s/physical-education" title="View Hunter College High School's Physical Education Teachers">Physical Education</a>,
 <a alt="View Sandra Miley's Ratings" class="btn view_more" href="/sandra-miley/262028-t" title="View Sandra Miley's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/sandra-miley/262028-t"></a>,
 <a alt="View Philip Frankel's Ratings" class="name" href="/philip-frankel/1875164-t" target="_blank" title="View Philip Frankel's Ratings">
 Philip Frankel
 </a>,
 <a href="/hunter-college-high-school/25767-s/science" title="View Hunter College High School's Science Teachers">Science</a>,
 <a alt="View Philip Frankel's Ratings" class="btn view_more" href="/philip-frankel/1875164-t" title="View Philip Frankel's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/philip-frankel/1875164-t"></a>,
 <a alt="View Lee Weinberg's Ratings" class="name" href="/lee-weinberg/337869-t" target="_blank" title="View Lee Weinberg's Ratings">
 Lee Weinberg
 </a>,
 <a href="/hunter-college-high-school/25767-s/counselor" title="View Hunter College High School's Counselor Teachers">Counselor</a>,
 <a alt="View Lee Weinberg's Ratings" class="btn view_more" href="/lee-weinberg/337869-t" title="View Lee Weinberg's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/lee-weinberg/337869-t"></a>,
 <a alt="View Eugene Lim's Ratings" class="name" href="/eugene-lim/1998685-t" target="_blank" title="View Eugene Lim's Ratings">
 Eugene Lim
 </a>,
 <a href="/hunter-college-high-school/25767-s/librarian" title="View Hunter College High School's Librarian Teachers">Librarian</a>,
 <a alt="View Eugene Lim's Ratings" class="btn view_more" href="/eugene-lim/1998685-t" title="View Eugene Lim's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/eugene-lim/1998685-t"></a>,
 <a alt="View Melinda Stepanski's Ratings" class="name" href="/melinda-stepanski/1845470-t" target="_blank" title="View Melinda Stepanski's Ratings">
 Melinda Stepanski
 </a>,
 <a href="/hunter-college-high-school/25767-s/english" title="View Hunter College High School's English Teachers">English</a>,
 <a alt="View Melinda Stepanski's Ratings" class="btn view_more" href="/melinda-stepanski/1845470-t" title="View Melinda Stepanski's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/melinda-stepanski/1845470-t"></a>,
 <a alt="View Pamela Lewis' Ratings" class="name" href="/pamela-lewis/172355-t" target="_blank" title="View Pamela Lewis' Ratings">
 Pamela Lewis
 </a>,
 <a href="/hunter-college-high-school/25767-s/languages" title="View Hunter College High School's Languages Teachers">Languages</a>,
 <a alt="View Pamela Lewis' Ratings" class="btn view_more" href="/pamela-lewis/172355-t" title="View Pamela Lewis' Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/pamela-lewis/172355-t"></a>,
 <a alt="View Anthony Natelli's Ratings" class="name" href="/anthony-natelli/1960538-t" target="_blank" title="View Anthony Natelli's Ratings">
 Anthony Natelli
 </a>,
 <a href="/hunter-college-high-school/25767-s/counselor" title="View Hunter College High School's Counselor Teachers">Counselor</a>,
 <a alt="View Anthony Natelli's Ratings" class="btn view_more" href="/anthony-natelli/1960538-t" title="View Anthony Natelli's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/anthony-natelli/1960538-t"></a>,
 <a alt="View Wallace's Ratings" class="name" href="/wallace/239035-t" target="_blank" title="View Wallace's Ratings">
 Mr. Wallace
 </a>,
 <a href="/hunter-college-high-school/25767-s/substitute-teacher" title="View Hunter College High School's Substitute Teacher Teachers">Substitute Teacher</a>,
 <a alt="View Wallace's Ratings" class="btn view_more" href="/wallace/239035-t" title="View Wallace's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/wallace/239035-t"></a>,
 <a alt="View Carolyn Mayadas' Ratings" class="name" href="/carolyn-mayadas/264965-t" target="_blank" title="View Carolyn Mayadas' Ratings">
 Carolyn Mayadas
 </a>,
 <a href="/hunter-college-high-school/25767-s/computer-science" title="View Hunter College High School's Computer Science Teachers">Computer Science</a>,
 <a alt="View Carolyn Mayadas' Ratings" class="btn view_more" href="/carolyn-mayadas/264965-t" title="View Carolyn Mayadas' Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/carolyn-mayadas/264965-t"></a>,
 <a alt="View Bob Sabin's Ratings" class="name" href="/bob-sabin/962015-t" target="_blank" title="View Bob Sabin's Ratings">
 Bob Sabin
 </a>,
 <a href="/hunter-college-high-school/25767-s/music" title="View Hunter College High School's Music Teachers">Music</a>,
 <a alt="View Bob Sabin's Ratings" class="btn view_more" href="/bob-sabin/962015-t" title="View Bob Sabin's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/bob-sabin/962015-t"></a>,
 <a alt="View Howard Adams' Ratings" class="name" href="/howard-adams/2074712-t" target="_blank" title="View Howard Adams' Ratings">
 Howard Adams
 </a>,
 <a href="/hunter-college-high-school/25767-s/physical-education" title="View Hunter College High School's Physical Education Teachers">Physical Education</a>,
 <a alt="View Howard Adams' Ratings" class="btn view_more" href="/howard-adams/2074712-t" title="View Howard Adams' Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/howard-adams/2074712-t"></a>,
 <a alt="View Eve Eisenstadt's Ratings" class="name" href="/eve-eisenstadt/246828-t" target="_blank" title="View Eve Eisenstadt's Ratings">
 Eve Eisenstadt
 </a>,
 <a href="/hunter-college-high-school/25767-s/visual-arts" title="View Hunter College High School's Visual Arts Teachers">Visual Arts</a>,
 <a alt="View Eve Eisenstadt's Ratings" class="btn view_more" href="/eve-eisenstadt/246828-t" title="View Eve Eisenstadt's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/eve-eisenstadt/246828-t"></a>,
 <a alt="View Kelly Honerkamp's Ratings" class="name" href="/kelly-honerkamp/7898685-t" target="_blank" title="View Kelly Honerkamp's Ratings">
 Kelly Honerkamp
 </a>,
 <a href="/hunter-college-high-school/25767-s/math" title="View Hunter College High School's Math Teachers">Math</a>,
 <a alt="View Kelly Honerkamp's Ratings" class="btn view_more" href="/kelly-honerkamp/7898685-t" title="View Kelly Honerkamp's Ratings">
 View More
 <i class="fa fa-angle-right"></i>
 </a>,
 <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/kelly-honerkamp/7898685-t"></a>,
 <a href="/hunter-college-high-school/25767-s" title="Page 1">1</a>,
 <a href="/hunter-college-high-school/25767-s/2" rel="next" title="Next Page">2</a>,
 <a href="/hunter-college-high-school/25767-s/3" title="Page 3">3</a>,
 <a href="/hunter-college-high-school/25767-s/2" rel="next" title="Next Page">
 <span class="hidden-sm hidden-md hidden-lg">
 <i class="fa fa-chevron-right"></i>
 </span>
 <span class="hidden-xs">
 <i class="fa fa-long-arrow-right"></i>
 </span>
 </a>,
 <a href="/hunter-college-high-school/25767-s/3" title="Last Page">
 <span class="hidden-sm hidden-md hidden-lg">
 <i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i>
 </span>
 <span class="hidden-xs">
 <i class="fa fa-angle-double-right"></i>
 </span>
 </a>,
 <a class="rating_histogram_widget_link_container" href="/hunter-college-high-school/25767-s/stats" title="Go to Hunter College High School stats">
 <div class="row block_container school_rating_histogram_card">
 <div class="col-xs-12">
 <h2 class="school_name" title="Learn more about Hunter College High School">
 <span>
 Hunter College High School Rating Histogram
 </span>
 </h2>
 <div class="score_line_container">
 <div class="score_label">5-star</div>
 <div class="score_percentage">69%</div>
 <div class="score_line">
 <div class="aux" style="width: 69.61%;"></div>
 </div>
 </div>
 <div class="score_line_container">
 <div class="score_label">4-star</div>
 <div class="score_percentage">14%</div>
 <div class="score_line">
 <div class="aux" style="width: 14.1%;"></div>
 </div>
 </div>
 <div class="score_line_container">
 <div class="score_label">3-star</div>
 <div class="score_percentage">8%</div>
 <div class="score_line">
 <div class="aux" style="width: 8.49%;"></div>
 </div>
 </div>
 <div class="score_line_container">
 <div class="score_label">2-star</div>
 <div class="score_percentage">2%</div>
 <div class="score_line">
 <div class="aux" style="width: 2.89%;"></div>
 </div>
 </div>
 <div class="score_line_container">
 <div class="score_label">1-star</div>
 <div class="score_percentage">4%</div>
 <div class="score_line">
 <div class="aux" style="width: 4.9%;"></div>
 </div>
 </div>
 <div class="score">
 <div class="rateit star-rating rateit-exclude" title="4.0 of 5">
 <div class="rateit-range" style="width: 90px; height: 15px;">
 <div class="rateit-preset rateit-selected" style="height: 15px; width: 71.517px;"></div>
 </div>
 </div>
 <span class="rating-summary">
 Based on
 4,301
 Ratings
 </span>
 </div>
 </div>
 </div>
 </a>,
 <a alt="Find Alaska's High Schools and Colleges" href="/alaska" title="Find Alaska's High Schools and Colleges">Alaska</a>,
 <a alt="Find Alabama's High Schools and Colleges" href="/alabama" title="Find Alabama's High Schools and Colleges">Alabama</a>,
 <a alt="Find Arkansas' High Schools and Colleges" href="/arkansas" title="Find Arkansas' High Schools and Colleges">Arkansas</a>,
 <a alt="Find Arizona's High Schools and Colleges" href="/arizona" title="Find Arizona's High Schools and Colleges">Arizona</a>,
 <a alt="Find California's High Schools and Colleges" href="/california" title="Find California's High Schools and Colleges">California</a>,
 <a alt="Find Colorado's High Schools and Colleges" href="/colorado" title="Find Colorado's High Schools and Colleges">Colorado</a>,
 <a alt="Find Connecticut's High Schools and Colleges" href="/connecticut" title="Find Connecticut's High Schools and Colleges">Connecticut</a>,
 <a alt="Find DC's High Schools and Colleges" href="/dc" title="Find DC's High Schools and Colleges">DC</a>,
 <a alt="Find Delaware's High Schools and Colleges" href="/delaware" title="Find Delaware's High Schools and Colleges">Delaware</a>,
 <a alt="Find Florida's High Schools and Colleges" href="/florida" title="Find Florida's High Schools and Colleges">Florida</a>,
 <a alt="Find Georgia's High Schools and Colleges" href="/georgia" title="Find Georgia's High Schools and Colleges">Georgia</a>,
 <a alt="Find Hawaii's High Schools and Colleges" href="/hawaii" title="Find Hawaii's High Schools and Colleges">Hawaii</a>,
 <a alt="Find Iowa's High Schools and Colleges" href="/iowa" title="Find Iowa's High Schools and Colleges">Iowa</a>,
 <a alt="Find Idaho's High Schools and Colleges" href="/idaho" title="Find Idaho's High Schools and Colleges">Idaho</a>,
 <a alt="Find Illinois' High Schools and Colleges" href="/illinois" title="Find Illinois' High Schools and Colleges">Illinois</a>,
 <a alt="Find Indiana's High Schools and Colleges" href="/indiana" title="Find Indiana's High Schools and Colleges">Indiana</a>,
 <a alt="Find Kansas' High Schools and Colleges" href="/kansas" title="Find Kansas' High Schools and Colleges">Kansas</a>,
 <a alt="Find Kentucky's High Schools and Colleges" href="/kentucky" title="Find Kentucky's High Schools and Colleges">Kentucky</a>,
 <a alt="Find Louisiana's High Schools and Colleges" href="/louisiana" title="Find Louisiana's High Schools and Colleges">Louisiana</a>,
 <a alt="Find Massachusetts' High Schools and Colleges" href="/massachusetts" title="Find Massachusetts' High Schools and Colleges">Massachusetts</a>,
 <a alt="Find Maryland's High Schools and Colleges" href="/maryland" title="Find Maryland's High Schools and Colleges">Maryland</a>,
 <a alt="Find Maine's High Schools and Colleges" href="/maine" title="Find Maine's High Schools and Colleges">Maine</a>,
 <a alt="Find Michigan's High Schools and Colleges" href="/michigan" title="Find Michigan's High Schools and Colleges">Michigan</a>,
 <a alt="Find Minnesota's High Schools and Colleges" href="/minnesota" title="Find Minnesota's High Schools and Colleges">Minnesota</a>,
 <a alt="Find Missouri's High Schools and Colleges" href="/missouri" title="Find Missouri's High Schools and Colleges">Missouri</a>,
 <a alt="Find Mississippi's High Schools and Colleges" href="/mississippi" title="Find Mississippi's High Schools and Colleges">Mississippi</a>,
 <a alt="Find Montana's High Schools and Colleges" href="/montana" title="Find Montana's High Schools and Colleges">Montana</a>,
 <a alt="Find North Carolina's High Schools and Colleges" href="/north-carolina" title="Find North Carolina's High Schools and Colleges">North Carolina</a>,
 <a alt="Find North Dakota's High Schools and Colleges" href="/north-dakota" title="Find North Dakota's High Schools and Colleges">North Dakota</a>,
 <a alt="Find Nebraska's High Schools and Colleges" href="/nebraska" title="Find Nebraska's High Schools and Colleges">Nebraska</a>,
 <a alt="Find New Hampshire's High Schools and Colleges" href="/new-hampshire" title="Find New Hampshire's High Schools and Colleges">New Hampshire</a>,
 <a alt="Find New Jersey's High Schools and Colleges" href="/new-jersey" title="Find New Jersey's High Schools and Colleges">New Jersey</a>,
 <a alt="Find New Mexico's High Schools and Colleges" href="/new-mexico" title="Find New Mexico's High Schools and Colleges">New Mexico</a>,
 <a alt="Find Nevada's High Schools and Colleges" href="/nevada" title="Find Nevada's High Schools and Colleges">Nevada</a>,
 <a alt="Find New York's High Schools and Colleges" href="/new-york" title="Find New York's High Schools and Colleges">New York</a>,
 <a alt="Find Ohio's High Schools and Colleges" href="/ohio" title="Find Ohio's High Schools and Colleges">Ohio</a>,
 <a alt="Find Oklahoma's High Schools and Colleges" href="/oklahoma" title="Find Oklahoma's High Schools and Colleges">Oklahoma</a>,
 <a alt="Find Oregon's High Schools and Colleges" href="/oregon" title="Find Oregon's High Schools and Colleges">Oregon</a>,
 <a alt="Find Pennsylvania's High Schools and Colleges" href="/pennsylvania" title="Find Pennsylvania's High Schools and Colleges">Pennsylvania</a>,
 <a alt="Find Puerto Rico's High Schools and Colleges" href="/puerto-rico" title="Find Puerto Rico's High Schools and Colleges">Puerto Rico</a>,
 <a alt="Find Rhode Island's High Schools and Colleges" href="/rhode-island" title="Find Rhode Island's High Schools and Colleges">Rhode Island</a>,
 <a alt="Find South Carolina's High Schools and Colleges" href="/south-carolina" title="Find South Carolina's High Schools and Colleges">South Carolina</a>,
 <a alt="Find South Dakota's High Schools and Colleges" href="/south-dakota" title="Find South Dakota's High Schools and Colleges">South Dakota</a>,
 <a alt="Find Tennessee's High Schools and Colleges" href="/tennessee" title="Find Tennessee's High Schools and Colleges">Tennessee</a>,
 <a alt="Find Texas' High Schools and Colleges" href="/texas" title="Find Texas' High Schools and Colleges">Texas</a>,
 <a alt="Find Utah's High Schools and Colleges" href="/utah" title="Find Utah's High Schools and Colleges">Utah</a>,
 <a alt="Find Virginia's High Schools and Colleges" href="/virginia" title="Find Virginia's High Schools and Colleges">Virginia</a>,
 <a alt="Find Vermont's High Schools and Colleges" href="/vermont" title="Find Vermont's High Schools and Colleges">Vermont</a>,
 <a alt="Find Washington's High Schools and Colleges" href="/washington" title="Find Washington's High Schools and Colleges">Washington</a>,
 <a alt="Find Wisconsin's High Schools and Colleges" href="/wisconsin" title="Find Wisconsin's High Schools and Colleges">Wisconsin</a>,
 <a alt="Find West Virginia's High Schools and Colleges" href="/west-virginia" title="Find West Virginia's High Schools and Colleges">West Virginia</a>,
 <a alt="Find Wyoming's High Schools and Colleges" href="/wyoming" title="Find Wyoming's High Schools and Colleges">Wyoming</a>,
 <a alt='Schools beginning with "A"' href="/schools/directory/a" title='Schools beginning with "A"'>a</a>,
 <a alt='Schools beginning with "B"' href="/schools/directory/b" title='Schools beginning with "B"'>b</a>,
 <a alt='Schools beginning with "C"' href="/schools/directory/c" title='Schools beginning with "C"'>c</a>,
 <a alt='Schools beginning with "D"' href="/schools/directory/d" title='Schools beginning with "D"'>d</a>,
 <a alt='Schools beginning with "E"' href="/schools/directory/e" title='Schools beginning with "E"'>e</a>,
 <a alt='Schools beginning with "F"' href="/schools/directory/f" title='Schools beginning with "F"'>f</a>,
 <a alt='Schools beginning with "G"' href="/schools/directory/g" title='Schools beginning with "G"'>g</a>,
 <a alt='Schools beginning with "H"' href="/schools/directory/h" title='Schools beginning with "H"'>h</a>,
 <a alt='Schools beginning with "I"' href="/schools/directory/i" title='Schools beginning with "I"'>i</a>,
 <a alt='Schools beginning with "J"' href="/schools/directory/j" title='Schools beginning with "J"'>j</a>,
 <a alt='Schools beginning with "K"' href="/schools/directory/k" title='Schools beginning with "K"'>k</a>,
 <a alt='Schools beginning with "L"' href="/schools/directory/l" title='Schools beginning with "L"'>l</a>,
 <a alt='Schools beginning with "M"' href="/schools/directory/m" title='Schools beginning with "M"'>m</a>,
 <a alt='Schools beginning with "N"' href="/schools/directory/n" title='Schools beginning with "N"'>n</a>,
 <a alt='Schools beginning with "O"' href="/schools/directory/o" title='Schools beginning with "O"'>o</a>,
 <a alt='Schools beginning with "P"' href="/schools/directory/p" title='Schools beginning with "P"'>p</a>,
 <a alt='Schools beginning with "Q"' href="/schools/directory/q" title='Schools beginning with "Q"'>q</a>,
 <a alt='Schools beginning with "R"' href="/schools/directory/r" title='Schools beginning with "R"'>r</a>,
 <a alt='Schools beginning with "S"' href="/schools/directory/s" title='Schools beginning with "S"'>s</a>,
 <a alt='Schools beginning with "T"' href="/schools/directory/t" title='Schools beginning with "T"'>t</a>,
 <a alt='Schools beginning with "U"' href="/schools/directory/u" title='Schools beginning with "U"'>u</a>,
 <a alt='Schools beginning with "V"' href="/schools/directory/v" title='Schools beginning with "V"'>v</a>,
 <a alt='Schools beginning with "W"' href="/schools/directory/w" title='Schools beginning with "W"'>w</a>,
 <a alt='Schools beginning with "X"' href="/schools/directory/x" title='Schools beginning with "X"'>x</a>,
 <a alt='Schools beginning with "Y"' href="/schools/directory/y" title='Schools beginning with "Y"'>y</a>,
 <a alt='Schools beginning with "Z"' href="/schools/directory/z" title='Schools beginning with "Z"'>z</a>,
 <a alt="Schools beginning with numbers" href="/schools/directory/%23" title="Schools beginning with numbers">#</a>,
 <a alt='Teachers beginning with "A"' href="/teachers/directory/a" title='Teachers beginning with "A"'>a</a>,
 <a alt='Teachers beginning with "B"' href="/teachers/directory/b" title='Teachers beginning with "B"'>b</a>,
 <a alt='Teachers beginning with "C"' href="/teachers/directory/c" title='Teachers beginning with "C"'>c</a>,
 <a alt='Teachers beginning with "D"' href="/teachers/directory/d" title='Teachers beginning with "D"'>d</a>,
 <a alt='Teachers beginning with "E"' href="/teachers/directory/e" title='Teachers beginning with "E"'>e</a>,
 <a alt='Teachers beginning with "F"' href="/teachers/directory/f" title='Teachers beginning with "F"'>f</a>,
 <a alt='Teachers beginning with "G"' href="/teachers/directory/g" title='Teachers beginning with "G"'>g</a>,
 <a alt='Teachers beginning with "H"' href="/teachers/directory/h" title='Teachers beginning with "H"'>h</a>,
 <a alt='Teachers beginning with "I"' href="/teachers/directory/i" title='Teachers beginning with "I"'>i</a>,
 <a alt='Teachers beginning with "J"' href="/teachers/directory/j" title='Teachers beginning with "J"'>j</a>,
 <a alt='Teachers beginning with "K"' href="/teachers/directory/k" title='Teachers beginning with "K"'>k</a>,
 <a alt='Teachers beginning with "L"' href="/teachers/directory/l" title='Teachers beginning with "L"'>l</a>,
 <a alt='Teachers beginning with "M"' href="/teachers/directory/m" title='Teachers beginning with "M"'>m</a>,
 <a alt='Teachers beginning with "N"' href="/teachers/directory/n" title='Teachers beginning with "N"'>n</a>,
 <a alt='Teachers beginning with "O"' href="/teachers/directory/o" title='Teachers beginning with "O"'>o</a>,
 <a alt='Teachers beginning with "P"' href="/teachers/directory/p" title='Teachers beginning with "P"'>p</a>,
 <a alt='Teachers beginning with "Q"' href="/teachers/directory/q" title='Teachers beginning with "Q"'>q</a>,
 <a alt='Teachers beginning with "R"' href="/teachers/directory/r" title='Teachers beginning with "R"'>r</a>,
 <a alt='Teachers beginning with "S"' href="/teachers/directory/s" title='Teachers beginning with "S"'>s</a>,
 <a alt='Teachers beginning with "T"' href="/teachers/directory/t" title='Teachers beginning with "T"'>t</a>,
 <a alt='Teachers beginning with "U"' href="/teachers/directory/u" title='Teachers beginning with "U"'>u</a>,
 <a alt='Teachers beginning with "V"' href="/teachers/directory/v" title='Teachers beginning with "V"'>v</a>,
 <a alt='Teachers beginning with "W"' href="/teachers/directory/w" title='Teachers beginning with "W"'>w</a>,
 <a alt='Teachers beginning with "X"' href="/teachers/directory/x" title='Teachers beginning with "X"'>x</a>,
 <a alt='Teachers beginning with "Y"' href="/teachers/directory/y" title='Teachers beginning with "Y"'>y</a>,
 <a alt='Teachers beginning with "Z"' href="/teachers/directory/z" title='Teachers beginning with "Z"'>z</a>,
 <a alt="United States" class="country" href="https://www.ratemyteachers.com" title="United States">United States</a>,
 <a alt="Canada" class="country" href="https://ca.ratemyteachers.com" title="Canada">Canada</a>,
 <a alt="United Kingdom" class="country" href="https://uk.ratemyteachers.com" title="United Kingdom">United Kingdom</a>,
 <a alt="Australia" class="country" href="https://au.ratemyteachers.com" title="Australia">Australia</a>,
 <a alt="New Zealand" class="country" href="https://nz.ratemyteachers.com" title="New Zealand">New Zealand</a>,
 <a alt="Ireland" class="country" href="https://ie.ratemyteachers.com" title="Ireland">Ireland</a>,
 <a alt="RateMyTeachers Frequently Asked Questions" href="/faq" title="RateMyTeachers Frequently Asked Questions">FAQ</a>,
 <a data-backdrop="static" data-keyboard="" data-remote="/contact/new" data-target="#modal" data-toggle="modal" href="javascript:void(0);" rel="nofollow" title="Contact RateMyTeachers">
 Contact
 </a>,
 <a href="/terms" title="RateMyTeachers Terms of Use">Terms of Use</a>,
 <a alt="RateMyTeachers Privacy Policy" href="/privacy" title="RateMyTeachers Privacy Policy">Privacy Policy</a>,
 <a href="/site-guidelines" title="RateMyTeachers Site Guidelines">Site Guidelines</a>,
 <a href="/copyright" title="RateMyTeachers Copyright Compliance">Copyright Compliance</a>,
 <a class="amp_clickurl amp_no_text" href="javascript:void(0);" rel="nofollow" target="_blank">
 <span class="amp_title"></span>
 <span class="amp_extension_merchant_rating" style="display: none;">
 <span class="amp_extension_merchant_rating_rating" data-star-width="18">
 <div class="rateit star-rating rateit-exclude" title="">
 <div class="rateit-range" style="width: 90px; height: 15px;">
 <div class="rateit-preset rateit-selected" style="height: 15px; width: 0.000px;"></div>
 </div>
 </div>
 </span>
 </span>
 <span class="amp_description"></span>
 <span class="amp_displayurl"></span>
 <img class="amp_impressionurl" style="height: 1px; width: 1px;"/>
 </a>,
 <a class="col-xs-6 amp_extension_site_links_link">
 <span class="amp_extension_site_links_text"></span>
 </a>,
 <a class="amp_clickurl amp_no_text" href="javascript:void(0);" rel="nofollow" target="_blank">
 <span class="amp_title"></span>
 <span class="amp_displayurl"></span>
 <span class="amp_extension_merchant_rating" style="display: none;">
 <span class="amp_extension_merchant_rating_rating" data-star-width="18">
 <div class="rateit star-rating rateit-exclude" title="">
 <div class="rateit-range" style="width: 90px; height: 15px;">
 <div class="rateit-preset rateit-selected" style="height: 15px; width: 0.000px;"></div>
 </div>
 </div>
 </span>
 </span>
 <span class="amp_description"></span>
 <img class="amp_impressionurl" style="height: 1px; width: 1px;"/>
 </a>,
 <a class="col-xs-6 amp_extension_site_links_link">
 <span class="amp_extension_site_links_text"></span>
 </a>]


### LOOK AT ONE DIV TAG

# So if I look at a
#    div tag, a single div tag, this is going to
#        return just one tag for me.

# So this is
#    returning the first div tag that it sees on the page.


# find finds the first instance of a specified tag
# returns a bs4 element


div_tag = results_page.find('div')
print(div_tag)

head_tag = results_page.find_all('title')
head_tag



##################################################
# results_page

<!DOCTYPE html>
<html>
 <head>
  <script type="text/javascript">
   (function(){
        window.beginTimeTrack = (new Date()).getTime();
      })();
  </script>
  <title>
   Hunter College High School - New York, New York | RateMyTeachers.com
  </title>
  <meta content="IE=edge" http-equiv="X-UA-Compatible"/>
  <meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
  <script type="text/javascript">
   window.NREUM||(NREUM={});NREUM.info={"beacon":"bam.nr-data.net","errorBeacon":"bam.nr-data.net","licenseKey":"f46052bf0f","applicationID":"3606589","transactionName":"c1lfF0sNXlRRFhxGAlhZXg9KTUFQWxM=","queueTime":0,"applicationTime":604,"agentToken":null,"agent":""}
  </script>
  <script type="text/javascript">
   (window.NREUM||(NREUM={})).loader_config={xpid:"VwEAU1VbGwAGVFdXDwg="};window.NREUM||(NREUM={}),__nr_require=function(t,e,n){function r(n){if(!e[n]){var o=e[n]={exports:{}};t[n][0].call(o.exports,function(e){var o=t[n][1][e];return r(o||e)},o,o.exports)}return e[n].exports}if("function"==typeof __nr_require)return __nr_require;for(var o=0;o<n.length;o++)r(n[o]);return r}({1:[function(t,e,n){function r(t){try{c.console&&console.log(t)}catch(e){}}var o,i=t("ee"),a=t(12),c={};try{o=localStorage.getItem("__nr_flags").split(","),console&&"function"==typeof console.log&&(c.console=!0,o.indexOf("dev")!==-1&&(c.dev=!0),o.indexOf("nr_dev")!==-1&&(c.nrDev=!0))}catch(s){}c.nrDev&&i.on("internal-error",function(t){r(t.stack)}),c.dev&&i.on("fn-err",function(t,e,n){r(n.stack)}),c.dev&&(r("NR AGENT IN DEVELOPMENT MODE"),r("flags: "+a(c,function(t,e){return t}).join(", ")))},{}],2:[function(t,e,n){function r(t,e,n,r,c){try{p?p-=1:o(c||new UncaughtException(t,e,n),!0)}catch(f){try{i("ierr",[f,s.now(),!0])}catch(d){}}return"function"==typeof u&&u.apply(this,a(arguments))}function UncaughtException(t,e,n){this.message=t||"Uncaught error with no additional information",this.sourceURL=e,this.line=n}function o(t,e){var n=e?null:s.now();i("err",[t,n])}var i=t("handle"),a=t(13),c=t("ee"),s=t("loader"),f=t("gos"),u=window.onerror,d=!1,l="nr@seenError",p=0;s.features.err=!0,t(1),window.onerror=r;try{throw new Error}catch(h){"stack"in h&&(t(5),t(4),"addEventListener"in window&&t(3),s.xhrWrappable&&t(6),d=!0)}c.on("fn-start",function(t,e,n){d&&(p+=1)}),c.on("fn-err",function(t,e,n){d&&!n[l]&&(f(n,l,function(){return!0}),this.thrown=!0,o(n))}),c.on("fn-end",function(){d&&!this.thrown&&p>0&&(p-=1)}),c.on("internal-error",function(t){i("ierr",[t,s.now(),!0])})},{}],3:[function(t,e,n){function r(t){for(var e=t;e&&!e.hasOwnProperty(u);)e=Object.getPrototypeOf(e);e&&o(e)}function o(t){c.inPlace(t,[u,d],"-",i)}function i(t,e){return t[1]}var a=t("ee").get("events"),c=t(15)(a,!0),s=t("gos"),f=XMLHttpRequest,u="addEventListener",d="removeEventListener";e.exports=a,"getPrototypeOf"in Object?(r(document),r(window),r(f.prototype)):f.prototype.hasOwnProperty(u)&&(o(window),o(f.prototype)),a.on(u+"-start",function(t,e){var n=t[1],r=s(n,"nr@wrapped",function(){function t(){if("function"==typeof n.handleEvent)return n.handleEvent.apply(n,arguments)}var e={object:t,"function":n}[typeof n];return e?c(e,"fn-",null,e.name||"anonymous"):n});this.wrapped=t[1]=r}),a.on(d+"-start",function(t){t[1]=this.wrapped||t[1]})},{}],4:[function(t,e,n){var r=t("ee").get("raf"),o=t(15)(r),i="equestAnimationFrame";e.exports=r,o.inPlace(window,["r"+i,"mozR"+i,"webkitR"+i,"msR"+i],"raf-"),r.on("raf-start",function(t){t[0]=o(t[0],"fn-")})},{}],5:[function(t,e,n){function r(t,e,n){t[0]=a(t[0],"fn-",null,n)}function o(t,e,n){this.method=n,this.timerDuration=isNaN(t[1])?0:+t[1],t[0]=a(t[0],"fn-",this,n)}var i=t("ee").get("timer"),a=t(15)(i),c="setTimeout",s="setInterval",f="clearTimeout",u="-start",d="-";e.exports=i,a.inPlace(window,[c,"setImmediate"],c+d),a.inPlace(window,[s],s+d),a.inPlace(window,[f,"clearImmediate"],f+d),i.on(s+u,r),i.on(c+u,o)},{}],6:[function(t,e,n){function r(t,e){d.inPlace(e,["onreadystatechange"],"fn-",c)}function o(){var t=this,e=u.context(t);t.readyState>3&&!e.resolved&&(e.resolved=!0,u.emit("xhr-resolved",[],t)),d.inPlace(t,w,"fn-",c)}function i(t){g.push(t),h&&(b?b.then(a):v?v(a):(E=-E,O.data=E))}function a(){for(var t=0;t<g.length;t++)r([],g[t]);g.length&&(g=[])}function c(t,e){return e}function s(t,e){for(var n in t)e[n]=t[n];return e}t(3);var f=t("ee"),u=f.get("xhr"),d=t(15)(u),l=NREUM.o,p=l.XHR,h=l.MO,m=l.PR,v=l.SI,y="readystatechange",w=["onload","onerror","onabort","onloadstart","onloadend","onprogress","ontimeout"],g=[];e.exports=u;var x=window.XMLHttpRequest=function(t){var e=new p(t);try{u.emit("new-xhr",[e],e),e.addEventListener(y,o,!1)}catch(n){try{u.emit("internal-error",[n])}catch(r){}}return e};if(s(p,x),x.prototype=p.prototype,d.inPlace(x.prototype,["open","send"],"-xhr-",c),u.on("send-xhr-start",function(t,e){r(t,e),i(e)}),u.on("open-xhr-start",r),h){var b=m&&m.resolve();if(!v&&!m){var E=1,O=document.createTextNode(E);new h(a).observe(O,{characterData:!0})}}else f.on("fn-end",function(t){t[0]&&t[0].type===y||a()})},{}],7:[function(t,e,n){function r(t){var e=this.params,n=this.metrics;if(!this.ended){this.ended=!0;for(var r=0;r<d;r++)t.removeEventListener(u[r],this.listener,!1);if(!e.aborted){if(n.duration=a.now()-this.startTime,4===t.readyState){e.status=t.status;var i=o(t,this.lastSize);if(i&&(n.rxSize=i),this.sameOrigin){var s=t.getResponseHeader("X-NewRelic-App-Data");s&&(e.cat=s.split(", ").pop())}}else e.status=0;n.cbTime=this.cbTime,f.emit("xhr-done",[t],t),c("xhr",[e,n,this.startTime])}}}function o(t,e){var n=t.responseType;if("json"===n&&null!==e)return e;var r="arraybuffer"===n||"blob"===n||"json"===n?t.response:t.responseText;return h(r)}function i(t,e){var n=s(e),r=t.params;r.host=n.hostname+":"+n.port,r.pathname=n.pathname,t.sameOrigin=n.sameOrigin}var a=t("loader");if(a.xhrWrappable){var c=t("handle"),s=t(8),f=t("ee"),u=["load","error","abort","timeout"],d=u.length,l=t("id"),p=t(11),h=t(10),m=window.XMLHttpRequest;a.features.xhr=!0,t(6),f.on("new-xhr",function(t){var e=this;e.totalCbs=0,e.called=0,e.cbTime=0,e.end=r,e.ended=!1,e.xhrGuids={},e.lastSize=null,p&&(p>34||p<10)||window.opera||t.addEventListener("progress",function(t){e.lastSize=t.loaded},!1)}),f.on("open-xhr-start",function(t){this.params={method:t[0]},i(this,t[1]),this.metrics={}}),f.on("open-xhr-end",function(t,e){"loader_config"in NREUM&&"xpid"in NREUM.loader_config&&this.sameOrigin&&e.setRequestHeader("X-NewRelic-ID",NREUM.loader_config.xpid)}),f.on("send-xhr-start",function(t,e){var n=this.metrics,r=t[0],o=this;if(n&&r){var i=h(r);i&&(n.txSize=i)}this.startTime=a.now(),this.listener=function(t){try{"abort"===t.type&&(o.params.aborted=!0),("load"!==t.type||o.called===o.totalCbs&&(o.onloadCalled||"function"!=typeof e.onload))&&o.end(e)}catch(n){try{f.emit("internal-error",[n])}catch(r){}}};for(var c=0;c<d;c++)e.addEventListener(u[c],this.listener,!1)}),f.on("xhr-cb-time",function(t,e,n){this.cbTime+=t,e?this.onloadCalled=!0:this.called+=1,this.called!==this.totalCbs||!this.onloadCalled&&"function"==typeof n.onload||this.end(n)}),f.on("xhr-load-added",function(t,e){var n=""+l(t)+!!e;this.xhrGuids&&!this.xhrGuids[n]&&(this.xhrGuids[n]=!0,this.totalCbs+=1)}),f.on("xhr-load-removed",function(t,e){var n=""+l(t)+!!e;this.xhrGuids&&this.xhrGuids[n]&&(delete this.xhrGuids[n],this.totalCbs-=1)}),f.on("addEventListener-end",function(t,e){e instanceof m&&"load"===t[0]&&f.emit("xhr-load-added",[t[1],t[2]],e)}),f.on("removeEventListener-end",function(t,e){e instanceof m&&"load"===t[0]&&f.emit("xhr-load-removed",[t[1],t[2]],e)}),f.on("fn-start",function(t,e,n){e instanceof m&&("onload"===n&&(this.onload=!0),("load"===(t[0]&&t[0].type)||this.onload)&&(this.xhrCbStart=a.now()))}),f.on("fn-end",function(t,e){this.xhrCbStart&&f.emit("xhr-cb-time",[a.now()-this.xhrCbStart,this.onload,e],e)})}},{}],8:[function(t,e,n){e.exports=function(t){var e=document.createElement("a"),n=window.location,r={};e.href=t,r.port=e.port;var o=e.href.split("://");!r.port&&o[1]&&(r.port=o[1].split("/")[0].split("@").pop().split(":")[1]),r.port&&"0"!==r.port||(r.port="https"===o[0]?"443":"80"),r.hostname=e.hostname||n.hostname,r.pathname=e.pathname,r.protocol=o[0],"/"!==r.pathname.charAt(0)&&(r.pathname="/"+r.pathname);var i=!e.protocol||":"===e.protocol||e.protocol===n.protocol,a=e.hostname===document.domain&&e.port===n.port;return r.sameOrigin=i&&(!e.hostname||a),r}},{}],9:[function(t,e,n){function r(){}function o(t,e,n){return function(){return i(t,[f.now()].concat(c(arguments)),e?null:this,n),e?void 0:this}}var i=t("handle"),a=t(12),c=t(13),s=t("ee").get("tracer"),f=t("loader"),u=NREUM;"undefined"==typeof window.newrelic&&(newrelic=u);var d=["setPageViewName","setCustomAttribute","setErrorHandler","finished","addToTrace","inlineHit","addRelease"],l="api-",p=l+"ixn-";a(d,function(t,e){u[e]=o(l+e,!0,"api")}),u.addPageAction=o(l+"addPageAction",!0),u.setCurrentRouteName=o(l+"routeName",!0),e.exports=newrelic,u.interaction=function(){return(new r).get()};var h=r.prototype={createTracer:function(t,e){var n={},r=this,o="function"==typeof e;return i(p+"tracer",[f.now(),t,n],r),function(){if(s.emit((o?"":"no-")+"fn-start",[f.now(),r,o],n),o)try{return e.apply(this,arguments)}catch(t){throw s.emit("fn-err",[arguments,this,t],n),t}finally{s.emit("fn-end",[f.now()],n)}}}};a("setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","),function(t,e){h[e]=o(p+e)}),newrelic.noticeError=function(t){"string"==typeof t&&(t=new Error(t)),i("err",[t,f.now()])}},{}],10:[function(t,e,n){e.exports=function(t){if("string"==typeof t&&t.length)return t.length;if("object"==typeof t){if("undefined"!=typeof ArrayBuffer&&t instanceof ArrayBuffer&&t.byteLength)return t.byteLength;if("undefined"!=typeof Blob&&t instanceof Blob&&t.size)return t.size;if(!("undefined"!=typeof FormData&&t instanceof FormData))try{return JSON.stringify(t).length}catch(e){return}}}},{}],11:[function(t,e,n){var r=0,o=navigator.userAgent.match(/Firefox[\/\s](\d+\.\d+)/);o&&(r=+o[1]),e.exports=r},{}],12:[function(t,e,n){function r(t,e){var n=[],r="",i=0;for(r in t)o.call(t,r)&&(n[i]=e(r,t[r]),i+=1);return n}var o=Object.prototype.hasOwnProperty;e.exports=r},{}],13:[function(t,e,n){function r(t,e,n){e||(e=0),"undefined"==typeof n&&(n=t?t.length:0);for(var r=-1,o=n-e||0,i=Array(o<0?0:o);++r<o;)i[r]=t[e+r];return i}e.exports=r},{}],14:[function(t,e,n){e.exports={exists:"undefined"!=typeof window.performance&&window.performance.timing&&"undefined"!=typeof window.performance.timing.navigationStart}},{}],15:[function(t,e,n){function r(t){return!(t&&t instanceof Function&&t.apply&&!t[a])}var o=t("ee"),i=t(13),a="nr@original",c=Object.prototype.hasOwnProperty,s=!1;e.exports=function(t,e){function n(t,e,n,o){function nrWrapper(){var r,a,c,s;try{a=this,r=i(arguments),c="function"==typeof n?n(r,a):n||{}}catch(f){l([f,"",[r,a,o],c])}u(e+"start",[r,a,o],c);try{return s=t.apply(a,r)}catch(d){throw u(e+"err",[r,a,d],c),d}finally{u(e+"end",[r,a,s],c)}}return r(t)?t:(e||(e=""),nrWrapper[a]=t,d(t,nrWrapper),nrWrapper)}function f(t,e,o,i){o||(o="");var a,c,s,f="-"===o.charAt(0);for(s=0;s<e.length;s++)c=e[s],a=t[c],r(a)||(t[c]=n(a,f?c+o:o,i,c))}function u(n,r,o){if(!s||e){var i=s;s=!0;try{t.emit(n,r,o,e)}catch(a){l([a,n,r,o])}s=i}}function d(t,e){if(Object.defineProperty&&Object.keys)try{var n=Object.keys(t);return n.forEach(function(n){Object.defineProperty(e,n,{get:function(){return t[n]},set:function(e){return t[n]=e,e}})}),e}catch(r){l([r])}for(var o in t)c.call(t,o)&&(e[o]=t[o]);return e}function l(e){try{t.emit("internal-error",e)}catch(n){}}return t||(t=o),n.inPlace=f,n.flag=a,n}},{}],ee:[function(t,e,n){function r(){}function o(t){function e(t){return t&&t instanceof r?t:t?s(t,c,i):i()}function n(n,r,o,i){if(!l.aborted||i){t&&t(n,r,o);for(var a=e(o),c=h(n),s=c.length,f=0;f<s;f++)c[f].apply(a,r);var d=u[w[n]];return d&&d.push([g,n,r,a]),a}}function p(t,e){y[t]=h(t).concat(e)}function h(t){return y[t]||[]}function m(t){return d[t]=d[t]||o(n)}function v(t,e){f(t,function(t,n){e=e||"feature",w[n]=e,e in u||(u[e]=[])})}var y={},w={},g={on:p,emit:n,get:m,listeners:h,context:e,buffer:v,abort:a,aborted:!1};return g}function i(){return new r}function a(){(u.api||u.feature)&&(l.aborted=!0,u=l.backlog={})}var c="nr@context",s=t("gos"),f=t(12),u={},d={},l=e.exports=o();l.backlog=u},{}],gos:[function(t,e,n){function r(t,e,n){if(o.call(t,e))return t[e];var r=n();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(t,e,{value:r,writable:!0,enumerable:!1}),r}catch(i){}return t[e]=r,r}var o=Object.prototype.hasOwnProperty;e.exports=r},{}],handle:[function(t,e,n){function r(t,e,n,r){o.buffer([t],r),o.emit(t,e,n)}var o=t("ee").get("handle");e.exports=r,r.ee=o},{}],id:[function(t,e,n){function r(t){var e=typeof t;return!t||"object"!==e&&"function"!==e?-1:t===window?0:a(t,i,function(){return o++})}var o=1,i="nr@id",a=t("gos");e.exports=r},{}],loader:[function(t,e,n){function r(){if(!b++){var t=x.info=NREUM.info,e=l.getElementsByTagName("script")[0];if(setTimeout(u.abort,3e4),!(t&&t.licenseKey&&t.applicationID&&e))return u.abort();f(w,function(e,n){t[e]||(t[e]=n)}),s("mark",["onload",a()+x.offset],null,"api");var n=l.createElement("script");n.src="https://"+t.agent,e.parentNode.insertBefore(n,e)}}function o(){"complete"===l.readyState&&i()}function i(){s("mark",["domContent",a()+x.offset],null,"api")}function a(){return E.exists&&performance.now?Math.round(performance.now()):(c=Math.max((new Date).getTime(),c))-x.offset}var c=(new Date).getTime(),s=t("handle"),f=t(12),u=t("ee"),d=window,l=d.document,p="addEventListener",h="attachEvent",m=d.XMLHttpRequest,v=m&&m.prototype;NREUM.o={ST:setTimeout,SI:d.setImmediate,CT:clearTimeout,XHR:m,REQ:d.Request,EV:d.Event,PR:d.Promise,MO:d.MutationObserver};var y=""+location,w={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",agent:"js-agent.newrelic.com/nr-1071.min.js"},g=m&&v&&v[p]&&!/CriOS/.test(navigator.userAgent),x=e.exports={offset:c,now:a,origin:y,features:{},xhrWrappable:g};t(9),l[p]?(l[p]("DOMContentLoaded",i,!1),d[p]("load",r,!1)):(l[h]("onreadystatechange",o),d[h]("onload",r)),s("mark",["firstbyte",c],null,"api");var b=0,E=t(14)},{}]},{},["loader",2,7]);
  </script>
  <meta content="width=device-width, initial-scale=1, minimum-scale=1.0, maximum-scale=1, user-scalable=no" name="viewport"/>
  <meta content="E797MgrWewAoj3f3d2qOtnwdjPZIXrkC0asUIbhlehw" name="google-site-verification"/>
  <meta content="Hunter College High School is a High School in New York, NY. Search Hunter College High School's ratings, statistics and reviews by students and parents." name="description"/>
  <meta content="https://www.ratemyteachers.com/images/logo_icon_1000.png" property="twitter:image"/>
  <meta content="https://www.ratemyteachers.com/images/logo_icon_1000.png" property="og:image"/>
  <meta content="Hunter College High School - New York, New York | RateMyTeachers.com" property="og:title"/>
  <meta content="rmt:school" property="og:type"/>
  <meta content="https://www.ratemyteachers.com/hunter-college-high-school/25767-s" property="og:url"/>
  <meta content="Hunter College High School - New York, New York | RateMyTeachers.com" property="og:site_name"/>
  <meta content="Hunter College High School is a High School in New York, NY. Search Hunter College High School's ratings, statistics and reviews by students and parents." property="og:description"/>
  <meta content="unsafe-url" name="referrer"/>
  <meta content="noodp,noydir" name="robots"/>
  <meta content="https://www.ratemyteachers.com/apple_touch_icon_196x196.png" property="rmt:image"/>
  <link href="/favicon.ico" rel="shortcut icon" sizes="64x64 48x48 32x32 16x16" type="image/x-icon"/>
  <link href="/apple_touch_icon_60x60.png" rel="apple-touch-icon"/>
  <link href="/apple_touch_icon_76x76.png" rel="apple-touch-icon" sizes="76x76"/>
  <link href="/apple_touch_icon_120x120.png" rel="apple-touch-icon" sizes="120x120"/>
  <link href="/apple_touch_icon_152x152.png" rel="apple-touch-icon" sizes="152x152"/>
  <link href="/apple_touch_icon_196x196.png" rel="apple-touch-icon-precomposed"/>
  <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"/>
  <link href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css" media="screen" rel="stylesheet"/>
  <link href="/assets/application-14a53ad0bb9a1fbc95784107ee093856.css" media="all" rel="stylesheet"/>
  <link href="https://code.jquery.com/ui/1.11.2/themes/smoothness/jquery-ui.css" rel="stylesheet"/>
  <script type="text/javascript">
   var currentState = 'NY';

  var siteConfig = {
    homepage_reload_tab: false,
    enableAnalytics:     true,
    debugMode:           false,
    asyncScripts:        true
  };


  function getWindowWidth() {
    var myWidth = 0, myHeight = 0;
    if( typeof( window.innerWidth ) === 'number' ) {
      myWidth = window.innerWidth; myHeight = window.innerHeight;
    } else if( document.documentElement && ( document.documentElement.clientWidth ||document.documentElement.clientHeight ) ) {
      myWidth = document.documentElement.clientWidth; myHeight = document.documentElement.clientHeight;
    } else if( document.body && ( document.body.clientWidth || document.body.clientHeight ) ) {
      myWidth = document.body.clientWidth; myHeight = document.body.clientHeight;
    }
    return myWidth;
  }

  var isDesktopVariant = true;
  var isTabletVariant = false;
  var isMobileVariant = false;
  var isExtraSmall = (getWindowWidth() < 768) || (screen ? screen.width < 768 : false);
  var isMobile = isExtraSmall || isMobileVariant;
  var isMedium = (getWindowWidth() < 1200) || (screen ? screen.width < 1200 : false);


  var isChrome = navigator.userAgent.indexOf('Chrome') > -1;
  var isExplorer = navigator.userAgent.indexOf('MSIE') > -1;
  var isFirefox = navigator.userAgent.indexOf('Firefox') > -1;
  var isSafari = navigator.userAgent.indexOf("Safari") > -1;
  var isOpera = navigator.userAgent.toLowerCase().indexOf("op") > -1;
  if ((isChrome)&&(isSafari)) {isSafari=false;}
  if ((isChrome)&&(isOpera)) {isChrome=false;}

  var enablePropel    = !isSafari && !isOpera && false;
  var enableMediabong = !isSafari && !isOpera;
  var enableBrightComedia = !isSafari && !isOpera;

  var isMobileUpload = false;

    var cseData = {
      isCseSearch: true
      ,paramFormat: '%{search_term}%{location}'
      ,stateList: [{"name":"Alaska","shortname":"ak"},{"name":"Alabama","shortname":"al"},{"name":"Arkansas","shortname":"ar"},{"name":"Arizona","shortname":"az"},{"name":"California","shortname":"ca"},{"name":"Colorado","shortname":"co"},{"name":"Connecticut","shortname":"ct"},{"name":"Dc","shortname":"dc"},{"name":"Delaware","shortname":"de"},{"name":"Florida","shortname":"fl"},{"name":"Georgia","shortname":"ga"},{"name":"Hawaii","shortname":"hi"},{"name":"Iowa","shortname":"ia"},{"name":"Idaho","shortname":"id"},{"name":"Illinois","shortname":"il"},{"name":"Indiana","shortname":"in"},{"name":"Kansas","shortname":"ks"},{"name":"Kentucky","shortname":"ky"},{"name":"Louisiana","shortname":"la"},{"name":"Massachusetts","shortname":"ma"},{"name":"Maryland","shortname":"md"},{"name":"Maine","shortname":"me"},{"name":"Michigan","shortname":"mi"},{"name":"Minnesota","shortname":"mn"},{"name":"Missouri","shortname":"mo"},{"name":"Mississippi","shortname":"ms"},{"name":"Montana","shortname":"mt"},{"name":"North Carolina","shortname":"nc"},{"name":"North Dakota","shortname":"nd"},{"name":"Nebraska","shortname":"ne"},{"name":"New Hampshire","shortname":"nh"},{"name":"New Jersey","shortname":"nj"},{"name":"New Mexico","shortname":"nm"},{"name":"Nevada","shortname":"nv"},{"name":"New York","shortname":"ny"},{"name":"Ohio","shortname":"oh"},{"name":"Oklahoma","shortname":"ok"},{"name":"Oregon","shortname":"or"},{"name":"Pennsylvania","shortname":"pa"},{"name":"Puerto Rico","shortname":"pr"},{"name":"Rhode Island","shortname":"ri"},{"name":"South Carolina","shortname":"sc"},{"name":"South Dakota","shortname":"sd"},{"name":"Tennessee","shortname":"tn"},{"name":"Texas","shortname":"tx"},{"name":"Utah","shortname":"ut"},{"name":"Virginia","shortname":"va"},{"name":"Vermont","shortname":"vt"},{"name":"Washington","shortname":"wa"},{"name":"Wisconsin","shortname":"wi"},{"name":"West Virginia","shortname":"wv"},{"name":"Wyoming","shortname":"wy"}]
    };


  // Search autocomplete widget
  var searchAutocompleteHTML = "<div class=\'desktop search_autocomplete_widget\'>\n<div class=\'autocomplete_teachers\'>\n<div class=\'autocomplete_subtitle\'>\n<i class=\'fa fa-user\'><\/i>\nTeachers and Professors\n<\/div>\n<div class=\'autocomplete_container\'>\n<div class=\'amp_ads_autocomplete_widget\' id=\'amp_ads_autocomplete\'><\/div>\n<div class=\'autocomplete_elements_container\'>\n<a class=\'autocomplete_element\' target=\'_blank\'>\n<span class=\'autocomplete_name\'><\/span>\n<span class=\'autocomplete_school_name\'><\/span>\n<\/a>\n<\/div>\n<\/div>\n<a class=\'autocomplete_view_more\'>\nView All\n<span class=\'autocomplete_count\'><\/span>\nTeachers and Professors\n<i class=\'fa fa-chevron-right\'><\/i>\n<\/a>\n<\/div>\n<div class=\'autocomplete_schools\'>\n<div class=\'autocomplete_subtitle\'>\n<i class=\'fa fa-university\'><\/i>\nSchools and Colleges\n<\/div>\n<div class=\'autocomplete_container\'>\n<div class=\'autocomplete_elements_container\'>\n<a class=\'autocomplete_element\' target=\'_blank\'>\n<span class=\'autocomplete_name\'><\/span>\n<span class=\'autocomplete_address\'><\/span>\n<\/a>\n<\/div>\n<\/div>\n<a class=\'autocomplete_view_more\'>\nView All\n<span class=\'autocomplete_count\'><\/span>\nSchools and Colleges\n<i class=\'fa fa-chevron-right\'><\/i>\n<\/a>\n<\/div>\n<\/div>\n";
  </script>
  <script type="text/javascript">
   // Async functions variable
  functionToLoad = [];
  
  // Fastest way to check if an object is an array
  functionToLoad.isArrayObj = function(obj) {
    return !!obj && obj.constructor === Array;
  };
  
  // Extract data from an element
  functionToLoad.extractElementData = function(elementData) {
    var data = {
      element: elementData
      ,async: false
      ,subElements: []
    };
    
    // The element is an array, check for async option
    if (this.isArrayObj(elementData) && elementData.length > 0) {
      data.async = !!elementData[1];
      data.element = elementData[0];
      data.subElements = elementData[2] || [];
    }
    return data;
  };
  
  // Wrap push functionality
  functionToLoad.realPush = functionToLoad.push;
  functionToLoad.executePush = function(args) {
    var data = this.extractElementData(args);

    // Inject script tag on inplace
    if (typeof data.element === 'string') {
      // Inject external file
      document.write('<script type="text/javascript" src="' + data.element + '"><\/script>');
    } else {
      // Inject function
      document.write('<script type="text/javascript">(');
      document.write(data.element.toString());
      document.write(')();<\/script>');
    }
    
    // Execute child scripts
    if (data.subElements.length > 0) {
      this.executePush(data.subElements);
    }
  };
  functionToLoad.push = function(args) {
    if (siteConfig.asyncScripts) {
      if (siteConfig.debugMode) { console.log('Async Script'); }
      
      // Async scripts so add it to array for later execution
      this.realPush(args);
      return;
    }
    if (siteConfig.debugMode) { console.log('Sync Script'); }
    
    // No async scripts, execute it right away
    this.executePush(args);
  };
  </script>
  <script type="text/javascript">
   _googlePush = function(a) {};
  </script>
  <script type="text/javascript">
   functionToLoad.push('//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js');
  functionToLoad.push('//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js');
  </script>
  <script>
   functionToLoad.push(function() {
        gaId = 'UA-4216499-1';

        (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
        (i[r].q=i[r].q||[]).push(arguments);},i[r].l=1*new Date();a=s.createElement(o),
        m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m);
        })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
        ga('create', gaId, 'auto');
        ga('require', 'displayfeatures');
        //ga('require', 'ecommerce', 'ecommerce.js');
      });
  </script>
  <script type="text/javascript">
   functionToLoad.push('/assets/rmt.analytics-b3702f400256546899eddf8b81076656.js');
  </script>
  <script>
   functionToLoad.push(function(){
    pageType = "";
    RMT.Analytics.trackPageview({dimensions: [{key: 'dimension1', value: pageType}]});
    searchTerm = "";
  });
  </script>
  <script type="text/javascript">
   // Returns a function, that, as long as it continues to be invoked, will not
    // be triggered. The function will be called after it stops being called for
    // N milliseconds. If `immediate` is passed, trigger the function on the
    // leading edge, instead of the trailing.
    function debounce(func, wait, immediate) {
      var timeout;
      return function() {
        var context = this, args = arguments;
        var later = function() {
          timeout = null;
          if (!immediate) func.apply(context, args);
        };
        var callNow = immediate && !timeout;
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
        if (callNow) func.apply(context, args);
      };
    };
  </script>
  <script data-cfasync="false" type="text/javascript">
   functionToLoad.push([function() {
    window.apd_options = { 'websiteId': 6292, 'runFromFrame': false };
    (function() {
      var w = window.apd_options.runFromFrame ? window.top : window;
      if(window.apd_options.runFromFrame && w!=window.parent) w=window.parent;
      if (w.location.hash.indexOf('apdAdmin') != -1){if(typeof(Storage) !== 'undefined') {w.localStorage.apdAdmin = 1;}}
      var adminMode = ((typeof(Storage) == 'undefined') || (w.localStorage.apdAdmin == 1));
      w.apd_options=window.apd_options;
      var apd = w.document.createElement('script'); apd.type = 'text/javascript'; apd.async = true;
      apd.src = '//' + (adminMode ? 'cdn' : 'ecdn') + '.firstimpression.io/' + (adminMode ? 'fi.js?id=' + window.apd_options.websiteId : 'fi_client.js') ;
      var s = w.document.getElementsByTagName('head')[0]; s.appendChild(apd);
    })();
  }, true]);
  </script>
  <script charset="utf-8" type="text/javascript">
   functionToLoad.push(function() {
        (function(G,o,O,g,L,e){G[g]=G[g]||function(){(G[g]['q']=G[g]['q']||[]).push(
        arguments)},G[g]['t']=1*new Date;L=o.createElement(O),e=o.getElementsByTagName(
        O)[0];L.async=1;L.src='//www.google.com/adsense/search/async-ads.js';
        e.parentNode.insertBefore(L,e)})(window,document,'script','_googCsa');
      });
  </script>
  <script type="text/javascript">
   functionToLoad.push('//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js');
  </script>
  <script type="text/javascript">
   functionToLoad.push(function() {
        window.deployads=[];
        window.deployads.push=function(){
          var b=document.querySelectorAll('script[type\x3d"text/x-ab-test"]:not([data-processed])');
          if(b&&0<b.length){
            var b=b[0];
            var a=b.innerHTML.replace(/xscript/g,"script");
            document.write(a);
            b.setAttribute("data-processed","true");
          }
        }
      });
  </script>
  <script type="text/javascript">
   functionToLoad.push(function() {

      var LazyAds = function(){
        // this.elements = {};
      };


      LazyAds.init = function(delay){
        this.elements = {};
        var self = this;
        if (typeof(delay) === 'undefined' || delay === null)
          delay = 10000;
        else
          console.info('Set LazyAds delay to ' + delay + 'ms');


        $(window).load(function() {
          // self.domLoaded = true;
          // console.log('LazyAds: window load');
          setTimeout(function() {
            self.domLoaded = true;
            self.refresh();
          }, delay);
          // self.refresh();
        });

        var scrollHandler = debounce(function(e){
          self.refresh();
        }, 100);
        jQuery(document).scroll(scrollHandler);
      };

      /* id:  can ben ID of en element, or a scroll offset */
      LazyAds.register = function(id, callback, opts) {
        // console.log('LazyAds: register ' + id);
        this.elements[ id ] = { loaded: false, callback: callback };
        this.refresh();
      };


      LazyAds.refresh = function() {
        var el, isVisible;
        var scrollY = window.scrollY;
        // console.log("LazyAds: scrollY " + scrollY);
        for(var id in this.elements) {
          if (!this.elements.hasOwnProperty(id)) continue;
          if(this.elements[id].loaded) continue;

          isVisible = false || this.domLoaded;

          if (!isVisible) {
            // handle scroll position
            if (/^\d+$/.test(id)) {
              // console.log('id is an offset');
              if( scrollY >= id ) {
                isVisible = true;
              }
            } else if( this.isVisible(id) ) {
              isVisible = true;
            }
          }

          if (isVisible) {
            this.elements[id].loaded = true;
            console.info('LazyAds: execute callback for ' + id);
            this.elements[id].callback();
            delete this.elements[id];
          }



        }
      };


      LazyAds.isVisible = function(id) {
        // https://github.com/customd/jquery-visible/blob/master/jquery.visible.js
        var $t        = $('#' + id);

        // if the id doesn't exist just bounce.
        if( !$t[0] ) return false;

        var $w        = $(window),  // todo refactor this
            t         = $t.get(0),
            vpWidth   = $w.width(),
            vpHeight  = $w.height(),
            direction = (direction) ? direction : 'both',
            clientSize = t.offsetWidth * t.offsetHeight;
            // clientSize = hidden === true ? t.offsetWidth * t.offsetHeight : true;

        if (typeof t.getBoundingClientRect === 'function'){

            // Use this native browser method, if available.
            var rec = t.getBoundingClientRect(),
                tViz = rec.top    >= 0 && rec.top    <  vpHeight,
                bViz = rec.bottom >  0 && rec.bottom <= vpHeight,
                lViz = rec.left   >= 0 && rec.left   <  vpWidth,
                rViz = rec.right  >  0 && rec.right  <= vpWidth,
                vVisible   = tViz || bViz,
                hVisible   = lViz || rViz;

            if(direction === 'both')
                return clientSize && vVisible && hVisible;
            else if(direction === 'vertical')
                return clientSize && vVisible;
            else if(direction === 'horizontal')
                return clientSize && hVisible;
        } else {

            var viewTop         = $w.scrollTop(),
                viewBottom      = viewTop + vpHeight,
                viewLeft        = $w.scrollLeft(),
                viewRight       = viewLeft + vpWidth,
                offset          = $t.offset(),
                _top            = offset.top,
                _bottom         = _top + $t.height(),
                _left           = offset.left,
                _right          = _left + $t.width(),
                compareTop      = _bottom,
                compareBottom   = _top,
                compareLeft     = _right,
                compareRight    = _left;

            if(direction === 'both')
                return !!clientSize && ((compareBottom <= viewBottom) && (compareTop >= viewTop)) && ((compareRight <= viewRight) && (compareLeft >= viewLeft));
            else if(direction === 'vertical')
                return !!clientSize && ((compareBottom <= viewBottom) && (compareTop >= viewTop));
            else if(direction === 'horizontal')
                return !!clientSize && ((compareRight <= viewRight) && (compareLeft >= viewLeft));
        }
      };



      var delay = null;
      LazyAds.init(delay);

      // (function() {
      //   var delay = null;
      //   LazyAds.init();
      // })();
    });
  </script>
  <script type="text/javascript">
   var _session = {};
  </script>
  <script type="text/javascript">
   functionToLoad.push(["//tags-cdn.deployads.com/a/ratemyteachers.com.js", true,[
        function() {
          (deployads = window.deployads || []).push({});
        }
      ]]);
  </script>
  <link href="https://www.ratemyteachers.com/hunter-college-high-school/25767-s.rss" rel="alternate" type="application/rss+xml"/>
  <meta content="authenticity_token" name="csrf-param"/>
  <meta content="dn2l7ManOssrdBNX1CXTUWEKJ0NLORJkO377tnApG54=" name="csrf-token"/>
 </head>
 <body class="inner_page school_page schools_v12_1 ">
  <div id="fb-root">
  </div>
  <div class="rate_my_teachers_international">
   <div class="container">
    <div class="row">
     <a alt="United States" class="country active" href="https://www.ratemyteachers.com" title="United States">
      United States
     </a>
     <a alt="Canada" class="country " href="https://ca.ratemyteachers.com" title="Canada">
      Canada
     </a>
     <a alt="United Kingdom" class="country " href="https://uk.ratemyteachers.com" title="United Kingdom">
      United Kingdom
     </a>
     <a alt="Australia" class="country " href="https://au.ratemyteachers.com" title="Australia">
      Australia
     </a>
     <a alt="New Zealand" class="country " href="https://nz.ratemyteachers.com" title="New Zealand">
      New Zealand
     </a>
     <a alt="Ireland" class="country " href="https://ie.ratemyteachers.com" title="Ireland">
      Ireland
     </a>
     <div class="pull-right user_top_nav">
     </div>
    </div>
   </div>
  </div>
  <header>
   <div class="container">
    <div class="row">
     <form action="/search_page" class="tab-form search_form trigger_to_main_search" method="get">
      <a alt="Go to RateMyTeachers Home" href="/" id="rate_my_teachers_logo" title="Go to RateMyTeachers Home">
      </a>
      <input name="search" type="hidden" value="teachers"/>
      <div class="search_inputs">
       <div class="bg">
        <div class="padding">
         <input class="search_input" name="q" placeholder="Search: School Name, City" type="text"/>
        </div>
        <div class="location">
         <select class="state" id="state" name="state">
          <option value="">
           Select a State
          </option>
          <option value="ak">
           Alaska - AK
          </option>
          <option value="al">
           Alabama - AL
          </option>
          <option value="ar">
           Arkansas - AR
          </option>
          <option value="az">
           Arizona - AZ
          </option>
          <option value="ca">
           California - CA
          </option>
          <option value="co">
           Colorado - CO
          </option>
          <option value="ct">
           Connecticut - CT
          </option>
          <option value="dc">
           Dc - DC
          </option>
          <option value="de">
           Delaware - DE
          </option>
          <option value="fl">
           Florida - FL
          </option>
          <option value="ga">
           Georgia - GA
          </option>
          <option value="hi">
           Hawaii - HI
          </option>
          <option value="ia">
           Iowa - IA
          </option>
          <option value="id">
           Idaho - ID
          </option>
          <option value="il">
           Illinois - IL
          </option>
          <option value="in">
           Indiana - IN
          </option>
          <option value="ks">
           Kansas - KS
          </option>
          <option value="ky">
           Kentucky - KY
          </option>
          <option value="la">
           Louisiana - LA
          </option>
          <option value="ma">
           Massachusetts - MA
          </option>
          <option value="md">
           Maryland - MD
          </option>
          <option value="me">
           Maine - ME
          </option>
          <option value="mi">
           Michigan - MI
          </option>
          <option value="mn">
           Minnesota - MN
          </option>
          <option value="mo">
           Missouri - MO
          </option>
          <option value="ms">
           Mississippi - MS
          </option>
          <option value="mt">
           Montana - MT
          </option>
          <option value="nc">
           North Carolina - NC
          </option>
          <option value="nd">
           North Dakota - ND
          </option>
          <option value="ne">
           Nebraska - NE
          </option>
          <option value="nh">
           New Hampshire - NH
          </option>
          <option value="nj">
           New Jersey - NJ
          </option>
          <option value="nm">
           New Mexico - NM
          </option>
          <option value="nv">
           Nevada - NV
          </option>
          <option value="ny">
           New York - NY
          </option>
          <option value="oh">
           Ohio - OH
          </option>
          <option value="ok">
           Oklahoma - OK
          </option>
          <option value="or">
           Oregon - OR
          </option>
          <option value="pa">
           Pennsylvania - PA
          </option>
          <option value="pr">
           Puerto Rico - PR
          </option>
          <option value="ri">
           Rhode Island - RI
          </option>
          <option value="sc">
           South Carolina - SC
          </option>
          <option value="sd">
           South Dakota - SD
          </option>
          <option value="tn">
           Tennessee - TN
          </option>
          <option value="tx">
           Texas - TX
          </option>
          <option value="ut">
           Utah - UT
          </option>
          <option value="va">
           Virginia - VA
          </option>
          <option value="vt">
           Vermont - VT
          </option>
          <option value="wa">
           Washington - WA
          </option>
          <option value="wi">
           Wisconsin - WI
          </option>
          <option value="wv">
           West Virginia - WV
          </option>
          <option value="wy">
           Wyoming - WY
          </option>
         </select>
        </div>
       </div>
       <div class="search_button">
        <button class="btn-search fa fa-search fa-3x" title="Search RateMyTeachers" type="submit">
        </button>
       </div>
      </div>
     </form>
    </div>
   </div>
  </header>
  <div class="container-fluid main-content">
   <div class="row">
    <section class="breadcrumbs container-fluid">
     <div class="row">
      <div class="container">
       <div class="col-sm-12">
        <ul class="list-inline collapsible_nav collapsible_nav_collapsed">
         <li class="toggle">
          <a href="javascript:void(0);" rel="nofollow">
           <i class="fa fa-bars">
           </i>
          </a>
         </li>
         <li class="collapse">
          <a href="/" title="Go to RateMyTeachers Home">
           United States
          </a>
         </li>
         <li class="always_show">
          <a alt="Go to Schools in New York" href="/new-york" title="Go to Schools in New York">
           New York
          </a>
         </li>
         <li class="collapse">
          <a alt="Go to Schools in New York" href="/new-york/new-york" title="Go to Schools in New York">
           New York
          </a>
         </li>
         <li class="always_show">
          <a alt="View Hunter College High School's Teachers" href="/hunter-college-high-school/25767-s" title="View Hunter College High School's Teachers">
           Hunter College High School
          </a>
         </li>
         <li class="always_show extra_option">
          <a class="new_teacher_trigger" data-backdrop="static" data-keyboard="" data-remote="/teachers/new?sid=25767" data-school="Hunter College High School" data-sender-name="School page breadcrumb" data-target="#modal" data-toggle="modal" href="javascript:void(0);" rel="nofollow" title="Add My Teacher">
           Add My Teacher
          </a>
         </li>
         <li class="always_show extra_option">
          <a class="new_school_rating_trigger" data-backdrop="static" data-keyboard="" data-remote="/school_ratings/new?sid=25767" data-school="Hunter College High School" data-sender-name="School page breadcrumb" data-target="#modal_rating" data-toggle="modal" href="javascript:void(0);" rel="nofollow" title="Rate My School">
           Rate My School
          </a>
         </li>
        </ul>
       </div>
      </div>
     </div>
    </section>
    <div class="container flash_container">
     <div class="row">
      <div class="col-xs-12">
       <div class="alert alert-danger" id="flash-error" style="display: none">
        <button class="close" data-dismiss="close" type="button">
         ×
        </button>
        <span>
        </span>
       </div>
       <div class="alert alert-warning" id="flash-alert" style="display: none">
        <button class="close" data-dismiss="close" type="button">
         ×
        </button>
        <span>
        </span>
       </div>
       <div class="alert alert-success" id="flash-success" style="display: none">
        <button class="close" data-dismiss="close" type="button">
         ×
        </button>
        <span>
        </span>
       </div>
       <div class="alert alert-info" id="flash-notice" style="display: none">
        <button class="close" data-dismiss="close" type="button">
         ×
        </button>
        <span>
        </span>
       </div>
      </div>
     </div>
    </div>
    <div id="content">
     <span class="dn" itemscope="" itemtype="https://data-vocabulary.org/Breadcrumb">
      <a href="https://www.ratemyteachers.com/new-york" itemprop="url">
       <span itemprop="title">
        New York
       </span>
      </a>
      <span itemscope="" itemtype="https://data-vocabulary.org/Breadcrumb">
       <a href="https://www.ratemyteachers.com/new-york/new-york" itemprop="url">
        <span itemprop="title">
         New York
        </span>
       </a>
      </span>
     </span>
     <div id="sortable_ad_trigger">
     </div>
     <div class="container" itemscope="" itemtype="https://schema.org/ProfilePage">
      <meta content="2018-03-03" itemprop="dateModified"/>
      <div class="dn" itemprop="aggregateRating" itemscope="" itemtype="https://schema.org/AggregateRating">
       <meta content="4301" itemprop="ratingCount"/>
       <meta content="4301" itemprop="reviewCount"/>
       <meta content="3.97318" itemprop="ratingValue"/>
       <meta content="5" itemprop="bestRating"/>
       <meta content="0" itemprop="worstRating"/>
      </div>
      <div class="row">
       <section class="col-md-12 content" itemprop="about" itemscope="" itemtype="https://schema.org/School">
        <div class="row secondary_data">
         <div class="col-xs-12 col-lg-9 primary_column">
          <div class="row school_info">
           <div class="col-xs-12 col-sm-7 main_info">
            <div class="row">
             <div class="col-xs-12">
              <div class="school_name">
               <h1 title="Hunter College High School">
                <span itemprop="name">
                 Hunter College High School
                </span>
                <div class="school_actions" data-name="Hunter College High School" data-sid="25767" data-status="-1" style="display:none;">
                </div>
               </h1>
               <a class="edit school_correction_trigger" data-backdrop="static" data-keyboard="" data-remote="/schools/correction?sid=25767" data-school="Hunter College High School" data-sender-name="School page Main" data-target="#modal" data-toggle="modal" href="javascript:void(0);" rel="nofollow" remote="" title="Submit a Correction">
                Edit
               </a>
              </div>
              <div class="score">
               <div class="rateit star-rating rateit-exclude" title="4.0 of 5">
                <div class="rateit-range" style="width: 110px; height: 18px;">
                 <div class="rateit-preset rateit-selected" style="height: 18px; width: 87.410px;">
                 </div>
                </div>
               </div>
               Average
3.97
based on
4,301
teacher ratings
              </div>
              <div class="description">
               <strong>
                Hunter College High School
               </strong>
               is located in New York, New York
with an average teacher rating of 3.97
stars. When comparing
Hunter College High School's teachers to other
teachers in the state of
New York, Hunter College High School's
teachers are
below
the average of
4.39
stars.
Hunter College High School ranks
546
amongst all High Schools
in the state of New York.
               <a href="/hunter-college-high-school/25767-s/stats" target="_blank">
                Learn More
               </a>
              </div>
             </div>
            </div>
           </div>
           <div class="col-xs-12 col-sm-4 details">
            <div class="aux">
             <h2 class="detail_item rate_school">
              <a class="new_school_rating_trigger" data-backdrop="static" data-keyboard="" data-remote="/school_ratings/new?sid=25767" data-sender-name="School page Main" data-target="#modal_rating" data-teacher="Hunter College High School" data-toggle="modal" href="javascript:void(0);" rel="nofollow" remote="" title="Submit Rating for Hunter College High School">
               <i class="fa fa-institution">
               </i>
               <span class="value">
                Rate Hunter College High School
               </span>
              </a>
             </h2>
             <div class="detail_item address">
              <a href="https://www.google.com/maps/search/71%20E%2094%20St%2C%20New%20York%2C%20New%20York%2010128%2C%20New%20York%2C%20New%20York%2C%2010128%2C%20United%20States" target="_blank" title="71 E 94 St, New York, New York 10128">
               <i class="fa fa-map-marker">
               </i>
               <span class="value">
                71 E 94 St, New York, New York 10128
               </span>
              </a>
             </div>
             <div class="detail_item phone">
              <a class="school_phone_trigger" data-phone="718-349-4000" href="javascript:void(0);">
               <i class="fa fa-phone">
               </i>
               <span itemprop="telephone">
                718-349-4000
               </span>
              </a>
             </div>
             <h2 class="detail_item district">
              <i class="fa fa-map">
              </i>
              City University of New York
             </h2>
             <div class="detail_item website">
              <a href="https://www.hunterschools.org/hs" rel="nofollow" target="_blank" title="https://www.hunterschools.org/hs">
               <i class="fa fa-globe">
               </i>
               <span itemprop="url">
                https://www.hunterschools.org/hs
               </span>
              </a>
             </div>
            </div>
            <span class="dn" itemprop="address" itemscope="" itemtype="https://schema.org/PostalAddress">
             <span itemprop="streetAddress">
              71 E 94 St
             </span>
             <span itemprop="addressLocality">
              New York
             </span>
             <span itemprop="addressRegion">
              NY
             </span>
             <span itemprop="postalCode">
              10128
             </span>
            </span>
           </div>
          </div>
          <div class="school_content">
           <div class="sticky_container_center">
            <div class="sticky_column">
             <div class="row">
              <div class="col-xs-12">
               <div class="filter_section">
                <div class="row subtitle">
                 <div class="col-xs-6">
                  <h2 class="active">
                   <a href="https://www.ratemyteachers.com/hunter-college-high-school/25767-s" title="View Hunter College High School's Teachers">
                    Faculty:
218
Teachers
                   </a>
                  </h2>
                 </div>
                 <div class="col-xs-6">
                  <h2 class="">
                   <a href="https://www.ratemyteachers.com/hunter-college-high-school/25767-s/school-reviews" title="View Hunter College High School's Reviews">
                    Hunter College High School
Reviews
                   </a>
                  </h2>
                 </div>
                </div>
                <div class="row search_form_container">
                 <form action="/hunter-college-high-school/25767-s" class="simple_form inline_form" id="school_search_by_teacher_form">
                  <div class="col-md-2 sort_options">
                   <select id="sort_by" name="sort_by">
                    <option value="">
                     Sort by
                    </option>
                    <option value="">
                    </option>
                    <option value="">
                     Latest Update
                    </option>
                    <option value="last_name">
                     Last Name
                    </option>
                    <option value="first_name">
                     First Name
                    </option>
                    <option value="avg_asc">
                     Average Rating: Low to High
                    </option>
                    <option value="avg_desc">
                     Average Rating: High to Low
                    </option>
                   </select>
                  </div>
                  <div class="simple_form inline_form">
                   <div class="col-md-9 text">
                    <input name="q" placeholder="Search by Teacher" type="text"/>
                   </div>
                   <div class="col-md-1 options">
                    <button class="btn fa fa-search fa-2x" name="commit" title="Search by Teacher" type="submit">
                    </button>
                   </div>
                  </div>
                 </form>
                </div>
                <div class="row extra">
                 <a class="col-xs-4 new_admin_request_trigger apply_admin" data-remote="/admin/new?sid=25767" data-school="Hunter College High School" data-sender="School page Mobile Search Form" data-target="#modal" data-toggle="modal" href="javascript:void(0);" rel="nofollow" title="Become Hunter College High School's Moderator">
                  <i class="fa fa-user-plus">
                  </i>
                  <span>
                   Become a Moderator!
                  </span>
                 </a>
                 <a class="col-xs-4 new_school_rating_trigger school_review" data-backdrop="static" data-keyboard="" data-remote="/school_ratings/new?sid=25767" data-sender-name="School page Search bar" data-target="#modal_rating" data-teacher="Hunter College High School" data-toggle="modal" href="javascript:void(0);" rel="nofollow" remote="" title="Submit Rating for Hunter College High School">
                  <i class="fa fa-institution">
                  </i>
                  <span>
                   Write a School Review
                  </span>
                 </a>
                 <a class="col-xs-4 new_teacher_trigger add_teacher" data-backdrop="static" data-keyboard="" data-remote="/teachers/new?sid=25767" data-school="Hunter College High School" data-sender-name="School page Mobile Search Form" data-target="#modal" data-toggle="modal" href="javascript:void(0);" rel="nofollow" title="Add My Teacher to Hunter College High School">
                  <i class="fa fa-user-plus">
                  </i>
                  <span>
                   Add Teacher
                  </span>
                 </a>
                </div>
               </div>
              </div>
             </div>
            </div>
           </div>
           <div class="teachers">
            <div class="ad_container AMP">
             <div id="amp_ads_bottom">
             </div>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View David Towber's Ratings" class="name" href="/david-towber/172358-t" target="_blank" title="View David Towber's Ratings">
                David Towber
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/visual-arts" title="View Hunter College High School's Visual Arts Teachers">
                Visual Arts
               </a>
              </div>
              <div class="teacher_actions" data-name="David Towber" data-sid="25767" data-status="-2" data-tid="172358" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.2 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 91.960px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               53 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               Mr. Towber is hilarious and amazing, he was very friendly and supportive. (I had him in 7th grade)
              </div>
              <div class="options">
               <a alt="View David Towber's Ratings" class="btn view_more" href="/david-towber/172358-t" title="View David Towber's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/david-towber/172358-t">
             </a>
            </div>
            <div class="ad_container taboola_video">
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Drew Adams' Ratings" class="name" href="/drew-adams/1078417-t" target="_blank" title="View Drew Adams' Ratings">
                Drew Adams
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/physical-education" title="View Hunter College High School's Physical Education Teachers">
                Physical Education
               </a>
              </div>
              <div class="teacher_actions" data-name="Drew Adams" data-sid="25767" data-status="-2" data-tid="1078417" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="3.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 66.660px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               15 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               not very helpful at all and shorttemppered really awesome track coach though
              </div>
              <div class="options">
               <a alt="View Drew Adams' Ratings" class="btn view_more" href="/drew-adams/1078417-t" title="View Drew Adams' Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/drew-adams/1078417-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Tom Scott's Ratings" class="name" href="/tom-scott/225880-t" target="_blank" title="View Tom Scott's Ratings">
                Tom Scott
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/science" title="View Hunter College High School's Science Teachers">
                Science
               </a>
              </div>
              <div class="teacher_actions" data-name="Tom Scott" data-sid="25767" data-status="-2" data-tid="225880" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.5 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 99.880px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               34 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               Mr. Scott is an amazing teacher and you should be happy to have him. He's always really clear about explaining stuff...
              </div>
              <div class="options">
               <a alt="View Tom Scott's Ratings" class="btn view_more" href="/tom-scott/225880-t" title="View Tom Scott's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/tom-scott/225880-t">
             </a>
            </div>
            <div class="ad_container ATF">
             <div id="School_ATF_Leaderboard" style="border: 0px solid blue; text-align: center;">
              <div class="ad-tag" data-ad-name="lead_desktop" data-ad-size="728x90" id="lead_desktop">
              </div>
             </div>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Micheline Beaudry's Ratings" class="name" href="/micheline-beaudry/239022-t" target="_blank" title="View Micheline Beaudry's Ratings">
                Micheline Beaudry
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/music" title="View Hunter College High School's Music Teachers">
                Music
               </a>
              </div>
              <div class="teacher_actions" data-name="Micheline Beaudry" data-sid="25767" data-status="-2" data-tid="239022" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="3.2 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 69.740px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               63 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               I have Ms. Beaudry for 8th grade music. As a musician, I can definitely say that she explains everything really well;...
              </div>
              <div class="options">
               <a alt="View Micheline Beaudry's Ratings" class="btn view_more" href="/micheline-beaudry/239022-t" title="View Micheline Beaudry's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/micheline-beaudry/239022-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Peter Melman's Ratings" class="name" href="/peter-melman/1747652-t" target="_blank" title="View Peter Melman's Ratings">
                Peter Melman
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/english" title="View Hunter College High School's English Teachers">
                English
               </a>
              </div>
              <div class="teacher_actions" data-name="Peter Melman" data-sid="25767" data-status="-2" data-tid="1747652" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.5 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 99.660px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               19 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               i miss him so much and he was the greatest teacher i've ever had
              </div>
              <div class="options">
               <a alt="View Peter Melman's Ratings" class="btn view_more" href="/peter-melman/1747652-t" title="View Peter Melman's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/peter-melman/1747652-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Ben Morgenroth's Ratings" class="name" href="/ben-morgenroth/3983117-t" target="_blank" title="View Ben Morgenroth's Ratings">
                Ben Morgenroth
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/math" title="View Hunter College High School's Math Teachers">
                Math
               </a>
              </div>
              <div class="teacher_actions" data-name="Ben Morgenroth" data-sid="25767" data-status="-2" data-tid="3983117" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="2.6 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 56.980px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               17 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               He give too much HW and makes us copy down all the questions. Srsly bro?
              </div>
              <div class="options">
               <a alt="View Ben Morgenroth's Ratings" class="btn view_more" href="/ben-morgenroth/3983117-t" title="View Ben Morgenroth's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/ben-morgenroth/3983117-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Eliza Kuberska's Ratings" class="name" href="/eliza-kuberska/193595-t" target="_blank" title="View Eliza Kuberska's Ratings">
                Eliza Kuberska
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/math" title="View Hunter College High School's Math Teachers">
                Math
               </a>
              </div>
              <div class="teacher_actions" data-name="Eliza Kuberska" data-sid="25767" data-status="-2" data-tid="193595" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.7 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 104.060px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               96 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               Ms. Kuberska is the best teacher I've had so far in Hunter. She is really nice, really helpful, and is good at...
              </div>
              <div class="options">
               <a alt="View Eliza Kuberska's Ratings" class="btn view_more" href="/eliza-kuberska/193595-t" title="View Eliza Kuberska's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/eliza-kuberska/193595-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Bradley Scalise's Ratings" class="name" href="/bradley-scalise/7918595-t" target="_blank" title="View Bradley Scalise's Ratings">
                Bradley Scalise
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/science" title="View Hunter College High School's Science Teachers">
                Science
               </a>
              </div>
              <div class="teacher_actions" data-name="Bradley Scalise" data-sid="25767" data-status="-2" data-tid="7918595" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="3.9 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 85.140px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               5 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               Mr. Scalise has a good understanding of what the students like and he teaches well. He's pretty chill and will always...
              </div>
              <div class="options">
               <a alt="View Bradley Scalise's Ratings" class="btn view_more" href="/bradley-scalise/7918595-t" title="View Bradley Scalise's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/bradley-scalise/7918595-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Larry Ling's Ratings" class="name" href="/larry-ling/237643-t" target="_blank" title="View Larry Ling's Ratings">
                Larry Ling
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/languages" title="View Hunter College High School's Languages Teachers">
                Languages
               </a>
              </div>
              <div class="teacher_actions" data-name="Larry Ling" data-sid="25767" data-status="-2" data-tid="237643" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.7 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 103.620px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               70 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               Great teacher, funny, nice guy
              </div>
              <div class="options">
               <a alt="View Larry Ling's Ratings" class="btn view_more" href="/larry-ling/237643-t" title="View Larry Ling's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/larry-ling/237643-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Richard Fulco's Ratings" class="name" href="/richard-fulco/1104609-t" target="_blank" title="View Richard Fulco's Ratings">
                Richard Fulco
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/english" title="View Hunter College High School's English Teachers">
                English
               </a>
              </div>
              <div class="teacher_actions" data-name="Richard Fulco" data-sid="25767" data-status="-2" data-tid="1104609" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="3.7 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 80.740px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               27 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               not a competent or interesting teacher but somehow the class flies by like it never happened. he's sometimes funny...
              </div>
              <div class="options">
               <a alt="View Richard Fulco's Ratings" class="btn view_more" href="/richard-fulco/1104609-t" title="View Richard Fulco's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/richard-fulco/1104609-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Elizabeth Fox's Ratings" class="name" href="/elizabeth-fox/231055-t" target="_blank" title="View Elizabeth Fox's Ratings">
                Elizabeth Fox
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/physical-education" title="View Hunter College High School's Physical Education Teachers">
                Physical Education
               </a>
              </div>
              <div class="teacher_actions" data-name="Elizabeth Fox" data-sid="25767" data-status="-2" data-tid="231055" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.9 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 106.920px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               45 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               I had Coach Fox for a semester in 7th grade and she was a good teacher. Although it felt a bit patronizing at times,...
              </div>
              <div class="options">
               <a alt="View Elizabeth Fox's Ratings" class="btn view_more" href="/elizabeth-fox/231055-t" title="View Elizabeth Fox's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/elizabeth-fox/231055-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Tony Fisher's Ratings" class="name" href="/tony-fisher/1681402-t" target="_blank" title="View Tony Fisher's Ratings">
                Tony Fisher
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/math" title="View Hunter College High School's Math Teachers">
                Math
               </a>
              </div>
              <div class="teacher_actions" data-name="Tony Fisher" data-sid="25767" data-status="-2" data-tid="1681402" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.3 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 95.260px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               12 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               Love his ties!!
              </div>
              <div class="options">
               <a alt="View Tony Fisher's Ratings" class="btn view_more" href="/tony-fisher/1681402-t" title="View Tony Fisher's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/tony-fisher/1681402-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Steve Borowka's Ratings" class="name" href="/steve-borowka/1655713-t" target="_blank" title="View Steve Borowka's Ratings">
                Steve Borowka
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/performing-arts" title="View Hunter College High School's Performing Arts Teachers">
                Performing Arts
               </a>
              </div>
              <div class="teacher_actions" data-name="Steve Borowka" data-sid="25767" data-status="-2" data-tid="1655713" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.6 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 100.540px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               14 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               Awesome classes...
              </div>
              <div class="options">
               <a alt="View Steve Borowka's Ratings" class="btn view_more" href="/steve-borowka/1655713-t" title="View Steve Borowka's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/steve-borowka/1655713-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Margaret Sturiano's Ratings" class="name" href="/margaret-sturiano/1371640-t" target="_blank" title="View Margaret Sturiano's Ratings">
                Margaret Sturiano
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/performing-arts" title="View Hunter College High School's Performing Arts Teachers">
                Performing Arts
               </a>
              </div>
              <div class="teacher_actions" data-name="Margaret Sturiano" data-sid="25767" data-status="-2" data-tid="1371640" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.7 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 103.180px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               61 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               LEGEND. PURE LEGEND
              </div>
              <div class="options">
               <a alt="View Margaret Sturiano's Ratings" class="btn view_more" href="/margaret-sturiano/1371640-t" title="View Margaret Sturiano's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/margaret-sturiano/1371640-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Sylvia Schaindlin's Ratings" class="name" href="/sylvia-schaindlin/242184-t" target="_blank" title="View Sylvia Schaindlin's Ratings">
                Sylvia Schaindlin
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/math" title="View Hunter College High School's Math Teachers">
                Math
               </a>
              </div>
              <div class="teacher_actions" data-name="Sylvia Schaindlin" data-sid="25767" data-status="-2" data-tid="242184" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="3.4 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 74.580px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               77 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               She's a really nice teacher, but she follows rules to the letter because she doesn't know the material well enough to...
              </div>
              <div class="options">
               <a alt="View Sylvia Schaindlin's Ratings" class="btn view_more" href="/sylvia-schaindlin/242184-t" title="View Sylvia Schaindlin's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/sylvia-schaindlin/242184-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Luke Batson's Ratings" class="name" href="/luke-batson/1352298-t" target="_blank" title="View Luke Batson's Ratings">
                Luke Batson
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/music" title="View Hunter College High School's Music Teachers">
                Music
               </a>
              </div>
              <div class="teacher_actions" data-name="Luke Batson" data-sid="25767" data-status="-2" data-tid="1352298" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="3.4 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 75.680px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               41 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               very strict and rude
              </div>
              <div class="options">
               <a alt="View Luke Batson's Ratings" class="btn view_more" href="/luke-batson/1352298-t" title="View Luke Batson's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/luke-batson/1352298-t">
             </a>
            </div>
            <div class="placements" style="border: 1px solid transparent;">
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Linda Aboody's Ratings" class="name" href="/linda-aboody/193569-t" target="_blank" title="View Linda Aboody's Ratings">
                Linda Aboody
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/math" title="View Hunter College High School's Math Teachers">
                Math
               </a>
              </div>
              <div class="teacher_actions" data-name="Linda Aboody" data-sid="25767" data-status="-2" data-tid="193569" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="3.7 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 82.060px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               101 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               Ms Aboody is often late or absent with little explanation. Many subjects are barely touched upon in class and feature...
              </div>
              <div class="options">
               <a alt="View Linda Aboody's Ratings" class="btn view_more" href="/linda-aboody/193569-t" title="View Linda Aboody's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/linda-aboody/193569-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Lourdie Castillo's Ratings" class="name" href="/lourdie-castillo/7911689-t" target="_blank" title="View Lourdie Castillo's Ratings">
                Lourdie Castillo
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/chemistry" title="View Hunter College High School's Chemistry Teachers">
                Chemistry
               </a>
              </div>
              <div class="teacher_actions" data-name="Lourdie Castillo" data-sid="25767" data-status="-2" data-tid="7911689" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="2.5 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 54.560px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               11 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               I think some people are being way too harsh. I do not think he is totally clueless although he has done some things...
              </div>
              <div class="options">
               <a alt="View Lourdie Castillo's Ratings" class="btn view_more" href="/lourdie-castillo/7911689-t" title="View Lourdie Castillo's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/lourdie-castillo/7911689-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Gregory Boyle's Ratings" class="name" href="/gregory-boyle/248077-t" target="_blank" title="View Gregory Boyle's Ratings">
                Gregory Boyle
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/social-studies" title="View Hunter College High School's Social Studies Teachers">
                Social Studies
               </a>
              </div>
              <div class="teacher_actions" data-name="Gregory Boyle" data-sid="25767" data-status="-2" data-tid="248077" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="3.7 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 80.960px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               51 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               A great teacher, but not very clear and DEFINITELY not good at explanations. Sometimes annoying and sometimes cryptic
              </div>
              <div class="options">
               <a alt="View Gregory Boyle's Ratings" class="btn view_more" href="/gregory-boyle/248077-t" title="View Gregory Boyle's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/gregory-boyle/248077-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Caitlin Samuel's Ratings" class="name" href="/caitlin-samuel/3993811-t" target="_blank" title="View Caitlin Samuel's Ratings">
                Caitlin Samuel
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/science" title="View Hunter College High School's Science Teachers">
                Science
               </a>
              </div>
              <div class="teacher_actions" data-name="Caitlin Samuel" data-sid="25767" data-status="-2" data-tid="3993811" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.5 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 98.560px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               18 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               Very nice, easygoing teacher
              </div>
              <div class="options">
               <a alt="View Caitlin Samuel's Ratings" class="btn view_more" href="/caitlin-samuel/3993811-t" title="View Caitlin Samuel's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/caitlin-samuel/3993811-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Kasumi Parker's Ratings" class="name" href="/kasumi-parker/2146288-t" target="_blank" title="View Kasumi Parker's Ratings">
                Kasumi Parker
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/english" title="View Hunter College High School's English Teachers">
                English
               </a>
              </div>
              <div class="teacher_actions" data-name="Kasumi Parker" data-sid="25767" data-status="-2" data-tid="2146288" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.3 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 94.600px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               18 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               Really nice and she never yells!
              </div>
              <div class="options">
               <a alt="View Kasumi Parker's Ratings" class="btn view_more" href="/kasumi-parker/2146288-t" title="View Kasumi Parker's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/kasumi-parker/2146288-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Michael Keleher's Ratings" class="name" href="/michael-keleher/7911691-t" target="_blank" title="View Michael Keleher's Ratings">
                Michael Keleher
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/french" title="View Hunter College High School's French Teachers">
                French
               </a>
              </div>
              <div class="teacher_actions" data-name="Michael Keleher" data-sid="25767" data-status="-2" data-tid="7911691" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.9 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 108.460px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               5 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               A great teacher
              </div>
              <div class="options">
               <a alt="View Michael Keleher's Ratings" class="btn view_more" href="/michael-keleher/7911691-t" title="View Michael Keleher's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/michael-keleher/7911691-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Audrey Maurer's Ratings" class="name" href="/audrey-maurer/2493647-t" target="_blank" title="View Audrey Maurer's Ratings">
                Audrey Maurer
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/french" title="View Hunter College High School's French Teachers">
                French
               </a>
              </div>
              <div class="teacher_actions" data-name="Audrey Maurer" data-sid="25767" data-status="-2" data-tid="2493647" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="3.9 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 85.140px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               24 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               A French and a Latin teacher, well done! Sort of strict though.
              </div>
              <div class="options">
               <a alt="View Audrey Maurer's Ratings" class="btn view_more" href="/audrey-maurer/2493647-t" title="View Audrey Maurer's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/audrey-maurer/2493647-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Olivia Byun's Ratings" class="name" href="/olivia-byun/8057509-t" target="_blank" title="View Olivia Byun's Ratings">
                Olivia Byun
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/drafting" title="View Hunter College High School's Drafting Teachers">
                Drafting
               </a>
              </div>
              <div class="teacher_actions" data-name="Olivia Byun" data-sid="25767" data-status="0" data-tid="8057509" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.3 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 95.260px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               3 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               She's really nice and helps you understand everything. She is really relatable too
              </div>
              <div class="options">
               <a alt="View Olivia Byun's Ratings" class="btn view_more" href="/olivia-byun/8057509-t" title="View Olivia Byun's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/olivia-byun/8057509-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Daniel Sangermano's Ratings" class="name" href="/daniel-sangermano/682137-t" target="_blank" title="View Daniel Sangermano's Ratings">
                Daniel Sangermano
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/fine-arts" title="View Hunter College High School's Fine Arts Teachers">
                Fine Arts
               </a>
              </div>
              <div class="teacher_actions" data-name="Daniel Sangermano" data-sid="25767" data-status="-2" data-tid="682137" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.8 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 105.160px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               38 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               Havent had him for long but he has the ability to make me into an artist
              </div>
              <div class="options">
               <a alt="View Daniel Sangermano's Ratings" class="btn view_more" href="/daniel-sangermano/682137-t" title="View Daniel Sangermano's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/daniel-sangermano/682137-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Carol Samuel's Ratings" class="name" href="/carol-samuel/1376051-t" target="_blank" title="View Carol Samuel's Ratings">
                Carol Samuel
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/substitute-teacher" title="View Hunter College High School's Substitute Teacher Teachers">
                Substitute Teacher
               </a>
              </div>
              <div class="teacher_actions" data-name="Carol Samuel" data-sid="25767" data-status="-2" data-tid="1376051" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.3 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 93.500px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               6 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               She's usually in a bad mood, but it's a class that you can basically do ANYTHING and get away with it. Seriously, you...
              </div>
              <div class="options">
               <a alt="View Carol Samuel's Ratings" class="btn view_more" href="/carol-samuel/1376051-t" title="View Carol Samuel's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/carol-samuel/1376051-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Claire Mazzola's Ratings" class="name" href="/claire-mazzola/193564-t" target="_blank" title="View Claire Mazzola's Ratings">
                Claire Mazzola
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/languages" title="View Hunter College High School's Languages Teachers">
                Languages
               </a>
              </div>
              <div class="teacher_actions" data-name="Claire Mazzola" data-sid="25767" data-status="-2" data-tid="193564" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.6 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 100.760px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               44 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               Her lessons are really engaging and she's very willing to help people outside of class. I was starting to get bored...
              </div>
              <div class="options">
               <a alt="View Claire Mazzola's Ratings" class="btn view_more" href="/claire-mazzola/193564-t" title="View Claire Mazzola's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/claire-mazzola/193564-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Satinder Jawanda's Ratings" class="name" href="/satinder-jawanda/826502-t" target="_blank" title="View Satinder Jawanda's Ratings">
                Satinder Jawanda
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/social-studies" title="View Hunter College High School's Social Studies Teachers">
                Social Studies
               </a>
              </div>
              <div class="teacher_actions" data-name="Satinder Jawanda" data-sid="25767" data-status="-2" data-tid="826502" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 87.340px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               47 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               She's a really professional teacher who knows what she is talking about. If you pay attention, you learn a lot from...
              </div>
              <div class="options">
               <a alt="View Satinder Jawanda's Ratings" class="btn view_more" href="/satinder-jawanda/826502-t" title="View Satinder Jawanda's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/satinder-jawanda/826502-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Nikki Weinstein's Ratings" class="name" href="/nikki-weinstein/1652812-t" target="_blank" title="View Nikki Weinstein's Ratings">
                Nikki Weinstein
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/english" title="View Hunter College High School's English Teachers">
                English
               </a>
              </div>
              <div class="teacher_actions" data-name="Nikki Weinstein" data-sid="25767" data-status="-2" data-tid="1652812" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="3.4 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 75.240px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               18 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               I hate this woman. She was the worst teacher I've ever had. She made me hate english forever. I really really...
              </div>
              <div class="options">
               <a alt="View Nikki Weinstein's Ratings" class="btn view_more" href="/nikki-weinstein/1652812-t" title="View Nikki Weinstein's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/nikki-weinstein/1652812-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Stacy Goldstein's Ratings" class="name" href="/stacy-goldstein/1643756-t" target="_blank" title="View Stacy Goldstein's Ratings">
                Stacy Goldstein
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/biology" title="View Hunter College High School's Biology Teachers">
                Biology
               </a>
              </div>
              <div class="teacher_actions" data-name="Stacy Goldstein" data-sid="25767" data-status="-2" data-tid="1643756" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.1 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 90.860px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               16 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               I really enjoy having her as my teacher!
              </div>
              <div class="options">
               <a alt="View Stacy Goldstein's Ratings" class="btn view_more" href="/stacy-goldstein/1643756-t" title="View Stacy Goldstein's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/stacy-goldstein/1643756-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Amelia Betancourt's Ratings" class="name" href="/amelia-betancourt/1643770-t" target="_blank" title="View Amelia Betancourt's Ratings">
                Amelia Betancourt
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/languages" title="View Hunter College High School's Languages Teachers">
                Languages
               </a>
              </div>
              <div class="teacher_actions" data-name="Amelia Betancourt" data-sid="25767" data-status="-2" data-tid="1643770" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.8 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 104.500px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               31 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               AMAZING. ALL I HAVE TO SAY
              </div>
              <div class="options">
               <a alt="View Amelia Betancourt's Ratings" class="btn view_more" href="/amelia-betancourt/1643770-t" title="View Amelia Betancourt's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/amelia-betancourt/1643770-t">
             </a>
            </div>
            <div class="placements" style="border: 1px solid transparent;">
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Michael Stratechuk's Ratings" class="name" href="/michael-stratechuk/234440-t" target="_blank" title="View Michael Stratechuk's Ratings">
                Michael Stratechuk
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/music" title="View Hunter College High School's Music Teachers">
                Music
               </a>
              </div>
              <div class="teacher_actions" data-name="Michael Stratechuk" data-sid="25767" data-status="-2" data-tid="234440" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.3 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 95.260px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               70 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               He is so funny and the best teacher in the music dept. His class was so much fun and I miss it!!! Tests are very...
              </div>
              <div class="options">
               <a alt="View Michael Stratechuk's Ratings" class="btn view_more" href="/michael-stratechuk/234440-t" title="View Michael Stratechuk's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/michael-stratechuk/234440-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Roni Mistriel's Ratings" class="name" href="/roni-mistriel/242967-t" target="_blank" title="View Roni Mistriel's Ratings">
                Roni Mistriel
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/physical-education" title="View Hunter College High School's Physical Education Teachers">
                Physical Education
               </a>
              </div>
              <div class="teacher_actions" data-name="Roni Mistriel" data-sid="25767" data-status="-2" data-tid="242967" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="3.5 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 77.000px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               42 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               Okay, so Mr. M is super lax about everything. He never makes us do the warm-ups like my current teacher. He's also...
              </div>
              <div class="options">
               <a alt="View Roni Mistriel's Ratings" class="btn view_more" href="/roni-mistriel/242967-t" title="View Roni Mistriel's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/roni-mistriel/242967-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Brian Park's Ratings" class="name" href="/brian-park/1683905-t" target="_blank" title="View Brian Park's Ratings">
                Brian Park
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/science" title="View Hunter College High School's Science Teachers">
                Science
               </a>
              </div>
              <div class="teacher_actions" data-name="Brian Park" data-sid="25767" data-status="-2" data-tid="1683905" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.7 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 102.520px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               56 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               Mr. Park is one of my favorite teachers!! He always cracks jokes in class and never bores us. He does move at a...
              </div>
              <div class="options">
               <a alt="View Brian Park's Ratings" class="btn view_more" href="/brian-park/1683905-t" title="View Brian Park's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/brian-park/1683905-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Kip Zegers' Ratings" class="name" href="/kip-zegers/246707-t" target="_blank" title="View Kip Zegers' Ratings">
                Kip Zegers
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/english" title="View Hunter College High School's English Teachers">
                English
               </a>
              </div>
              <div class="teacher_actions" data-name="Kip Zegers" data-sid="25767" data-status="-2" data-tid="246707" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="3.5 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 76.560px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               60 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               THE BEST TEACHER I WILL EVER HAVE IN MY LIFE
              </div>
              <div class="options">
               <a alt="View Kip Zegers' Ratings" class="btn view_more" href="/kip-zegers/246707-t" title="View Kip Zegers' Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/kip-zegers/246707-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Melissa Chapnick's Ratings" class="name" href="/melissa-chapnick/1353338-t" target="_blank" title="View Melissa Chapnick's Ratings">
                Melissa Chapnick
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/social-studies" title="View Hunter College High School's Social Studies Teachers">
                Social Studies
               </a>
              </div>
              <div class="teacher_actions" data-name="Melissa Chapnick" data-sid="25767" data-status="-2" data-tid="1353338" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.4 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 97.460px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               33 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               she was my official teacher, she seems very nice!!
              </div>
              <div class="options">
               <a alt="View Melissa Chapnick's Ratings" class="btn view_more" href="/melissa-chapnick/1353338-t" title="View Melissa Chapnick's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/melissa-chapnick/1353338-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Sarah Fogelman's Ratings" class="name" href="/sarah-fogelman/486096-t" target="_blank" title="View Sarah Fogelman's Ratings">
                Sarah Fogelman
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/science" title="View Hunter College High School's Science Teachers">
                Science
               </a>
              </div>
              <div class="teacher_actions" data-name="Sarah Fogelman" data-sid="25767" data-status="-2" data-tid="486096" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.3 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 94.820px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               70 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               good teahcer :DD
              </div>
              <div class="options">
               <a alt="View Sarah Fogelman's Ratings" class="btn view_more" href="/sarah-fogelman/486096-t" title="View Sarah Fogelman's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/sarah-fogelman/486096-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Jana Lucash's Ratings" class="name" href="/jana-lucash/271302-t" target="_blank" title="View Jana Lucash's Ratings">
                Jana Lucash
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/social-studies" title="View Hunter College High School's Social Studies Teachers">
                Social Studies
               </a>
              </div>
              <div class="teacher_actions" data-name="Jana Lucash" data-sid="25767" data-status="-2" data-tid="271302" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.5 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 98.780px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               78 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               Ms. Lucash is so great!!! she just wants you to do your best and bring out the best from you. She clearly knows what...
              </div>
              <div class="options">
               <a alt="View Jana Lucash's Ratings" class="btn view_more" href="/jana-lucash/271302-t" title="View Jana Lucash's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/jana-lucash/271302-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Sheila Garcia's Ratings" class="name" href="/sheila-garcia/312565-t" target="_blank" title="View Sheila Garcia's Ratings">
                Sheila Garcia
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/counselor" title="View Hunter College High School's Counselor Teachers">
                Counselor
               </a>
              </div>
              <div class="teacher_actions" data-name="Sheila Garcia" data-sid="25767" data-status="-2" data-tid="312565" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="2.9 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 63.360px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               21 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               OMG I LOVE MS. GARCIA SHES SO NICE!!!
              </div>
              <div class="options">
               <a alt="View Sheila Garcia's Ratings" class="btn view_more" href="/sheila-garcia/312565-t" title="View Sheila Garcia's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/sheila-garcia/312565-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Rembert Herbert's Ratings" class="name" href="/rembert-herbert/211443-t" target="_blank" title="View Rembert Herbert's Ratings">
                Rembert Herbert
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/english" title="View Hunter College High School's English Teachers">
                English
               </a>
              </div>
              <div class="teacher_actions" data-name="Rembert Herbert" data-sid="25767" data-status="-2" data-tid="211443" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.8 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 106.040px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               51 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               Very good teacher!! Taught me a lot and allowed me to write the essay in a much looser format to allow for more...
              </div>
              <div class="options">
               <a alt="View Rembert Herbert's Ratings" class="btn view_more" href="/rembert-herbert/211443-t" title="View Rembert Herbert's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/rembert-herbert/211443-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Martha Curtis' Ratings" class="name" href="/martha-curtis/234435-t" target="_blank" title="View Martha Curtis' Ratings">
                Martha Curtis
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/social-studies" title="View Hunter College High School's Social Studies Teachers">
                Social Studies
               </a>
              </div>
              <div class="teacher_actions" data-name="Martha Curtis" data-sid="25767" data-status="-2" data-tid="234435" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.1 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 89.980px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               55 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               what a woman. goddess
              </div>
              <div class="options">
               <a alt="View Martha Curtis' Ratings" class="btn view_more" href="/martha-curtis/234435-t" title="View Martha Curtis' Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/martha-curtis/234435-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Lillian Drvostep's Ratings" class="name" href="/lillian-drvostep/229540-t" target="_blank" title="View Lillian Drvostep's Ratings">
                Lillian Drvostep
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/health" title="View Hunter College High School's Health Teachers">
                Health
               </a>
              </div>
              <div class="teacher_actions" data-name="Lillian Drvostep" data-sid="25767" data-status="-2" data-tid="229540" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="3.3 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 72.380px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               28 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               UGH! She is NEVER here. In seventh grade, we have only seen her twice and then heard she left the school. She was ok,...
              </div>
              <div class="options">
               <a alt="View Lillian Drvostep's Ratings" class="btn view_more" href="/lillian-drvostep/229540-t" title="View Lillian Drvostep's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/lillian-drvostep/229540-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Constance Rich's Ratings" class="name" href="/constance-rich/193686-t" target="_blank" title="View Constance Rich's Ratings">
                Constance Rich
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/visual-arts" title="View Hunter College High School's Visual Arts Teachers">
                Visual Arts
               </a>
              </div>
              <div class="teacher_actions" data-name="Constance Rich" data-sid="25767" data-status="-2" data-tid="193686" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.6 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 100.760px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               40 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               We had her last semester, great teacher who assigns reasonable homework, doesn't give pop quizzes, grades fairly and...
              </div>
              <div class="options">
               <a alt="View Constance Rich's Ratings" class="btn view_more" href="/constance-rich/193686-t" title="View Constance Rich's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/constance-rich/193686-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Irving Kagan's Ratings" class="name" href="/irving-kagan/234414-t" target="_blank" title="View Irving Kagan's Ratings">
                Irving Kagan
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/social-studies" title="View Hunter College High School's Social Studies Teachers">
                Social Studies
               </a>
              </div>
              <div class="teacher_actions" data-name="Irving Kagan" data-sid="25767" data-status="-2" data-tid="234414" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.6 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 100.540px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               36 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               he's legit just there to help you. if you don't even have him anymore but have a question about something in your own...
              </div>
              <div class="options">
               <a alt="View Irving Kagan's Ratings" class="btn view_more" href="/irving-kagan/234414-t" title="View Irving Kagan's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/irving-kagan/234414-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Betty Kleinfeld's Ratings" class="name" href="/betty-kleinfeld/323464-t" target="_blank" title="View Betty Kleinfeld's Ratings">
                Betty Kleinfeld
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/social-studies" title="View Hunter College High School's Social Studies Teachers">
                Social Studies
               </a>
              </div>
              <div class="teacher_actions" data-name="Betty Kleinfeld" data-sid="25767" data-status="-2" data-tid="323464" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="3.7 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 81.620px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               15 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               she has not updated her tests since the 70s when she probably first started teaching. the questions are never about...
              </div>
              <div class="options">
               <a alt="View Betty Kleinfeld's Ratings" class="btn view_more" href="/betty-kleinfeld/323464-t" title="View Betty Kleinfeld's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/betty-kleinfeld/323464-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View David Joffe's Ratings" class="name" href="/david-joffe/1340051-t" target="_blank" title="View David Joffe's Ratings">
                David Joffe
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/social-studies" title="View Hunter College High School's Social Studies Teachers">
                Social Studies
               </a>
              </div>
              <div class="teacher_actions" data-name="David Joffe" data-sid="25767" data-status="-2" data-tid="1340051" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.8 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 105.160px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               31 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               Such a smart guy who cares about what he's teaching. Take AFAM and your life will change- most eye opening class I've...
              </div>
              <div class="options">
               <a alt="View David Joffe's Ratings" class="btn view_more" href="/david-joffe/1340051-t" title="View David Joffe's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/david-joffe/1340051-t">
             </a>
            </div>
            <div class="placements" style="border: 1px solid transparent;">
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Rebecca Hollander's Ratings" class="name" href="/rebecca-hollander/234520-t" target="_blank" title="View Rebecca Hollander's Ratings">
                Rebecca Hollander
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/communications" title="View Hunter College High School's Communications Teachers">
                Communications
               </a>
              </div>
              <div class="teacher_actions" data-name="Rebecca Hollander" data-sid="25767" data-status="-2" data-tid="234520" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.1 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 89.540px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               50 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               Dr. Deans has changed my life! Great teacher and really cares about us.
              </div>
              <div class="options">
               <a alt="View Rebecca Hollander's Ratings" class="btn view_more" href="/rebecca-hollander/234520-t" title="View Rebecca Hollander's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/rebecca-hollander/234520-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Sheila Krilov's Ratings" class="name" href="/sheila-krilov/234397-t" target="_blank" title="View Sheila Krilov's Ratings">
                Sheila Krilov
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/math" title="View Hunter College High School's Math Teachers">
                Math
               </a>
              </div>
              <div class="teacher_actions" data-name="Sheila Krilov" data-sid="25767" data-status="-2" data-tid="234397" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.6 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 101.420px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               57 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               I love Ms. Krilov. However, I do not completely love her class. It's boring and often repetitive (although me being...
              </div>
              <div class="options">
               <a alt="View Sheila Krilov's Ratings" class="btn view_more" href="/sheila-krilov/234397-t" title="View Sheila Krilov's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/sheila-krilov/234397-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Bob Gaudenzi's Ratings" class="name" href="/bob-gaudenzi/244030-t" target="_blank" title="View Bob Gaudenzi's Ratings">
                Bob Gaudenzi
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/physical-education" title="View Hunter College High School's Physical Education Teachers">
                Physical Education
               </a>
              </div>
              <div class="teacher_actions" data-name="Bob Gaudenzi" data-sid="25767" data-status="-2" data-tid="244030" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.4 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 96.360px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               29 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               he is my swim coach and I love him! he is so sweet and understanding, even though I am pretty slow. would definitely...
              </div>
              <div class="options">
               <a alt="View Bob Gaudenzi's Ratings" class="btn view_more" href="/bob-gaudenzi/244030-t" title="View Bob Gaudenzi's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/bob-gaudenzi/244030-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Christopher Unruh's Ratings" class="name" href="/christopher-unruh/529880-t" target="_blank" title="View Christopher Unruh's Ratings">
                Christopher Unruh
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/languages" title="View Hunter College High School's Languages Teachers">
                Languages
               </a>
              </div>
              <div class="teacher_actions" data-name="Christopher Unruh" data-sid="25767" data-status="-2" data-tid="529880" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.6 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 101.200px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               35 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               love this man omg. cannot describe how fun latin is because of him. love him. his sense of style is also great I want...
              </div>
              <div class="options">
               <a alt="View Christopher Unruh's Ratings" class="btn view_more" href="/christopher-unruh/529880-t" title="View Christopher Unruh's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/christopher-unruh/529880-t">
             </a>
            </div>
            <div class="ad_container MID">
             <div class="sponsor" id="School_MID_Leaderboard">
              <div class="ad-tag" data-ad-name="mrec_desktop" data-ad-size="300x250" id="mrec_desktop">
              </div>
             </div>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Ray Kaniatyn's Ratings" class="name" href="/ray-kaniatyn/242188-t" target="_blank" title="View Ray Kaniatyn's Ratings">
                Ray Kaniatyn
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/physical-education" title="View Hunter College High School's Physical Education Teachers">
                Physical Education
               </a>
              </div>
              <div class="teacher_actions" data-name="Ray Kaniatyn" data-sid="25767" data-status="-2" data-tid="242188" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="3.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 66.000px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               40 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               I don't know why Coach K is getting such bad reviews!! Yes he was a little put off if you forgot something, but...
              </div>
              <div class="options">
               <a alt="View Ray Kaniatyn's Ratings" class="btn view_more" href="/ray-kaniatyn/242188-t" title="View Ray Kaniatyn's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/ray-kaniatyn/242188-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Thomas Keenan's Ratings" class="name" href="/thomas-keenan/478475-t" target="_blank" title="View Thomas Keenan's Ratings">
                Thomas Keenan
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/science" title="View Hunter College High School's Science Teachers">
                Science
               </a>
              </div>
              <div class="teacher_actions" data-name="Thomas Keenan" data-sid="25767" data-status="-2" data-tid="478475" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.7 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 104.060px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               47 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               good teacher, but seems really snooty and stuck-up as a person. the tests were easy if you studied. harsh grader on...
              </div>
              <div class="options">
               <a alt="View Thomas Keenan's Ratings" class="btn view_more" href="/thomas-keenan/478475-t" title="View Thomas Keenan's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/thomas-keenan/478475-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Clare Kudera's Ratings" class="name" href="/clare-kudera/232426-t" target="_blank" title="View Clare Kudera's Ratings">
                Clare Kudera
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/social-studies" title="View Hunter College High School's Social Studies Teachers">
                Social Studies
               </a>
              </div>
              <div class="teacher_actions" data-name="Clare Kudera" data-sid="25767" data-status="-2" data-tid="232426" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="3.8 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 83.820px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               82 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               MS. Kudera is scary, and definitely assigns insane amounts for homework which kids spend 4-5 hours on. Then the next...
              </div>
              <div class="options">
               <a alt="View Clare Kudera's Ratings" class="btn view_more" href="/clare-kudera/232426-t" title="View Clare Kudera's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/clare-kudera/232426-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Rebecca Ramirez's Ratings" class="name" href="/rebecca-ramirez/1638618-t" target="_blank" title="View Rebecca Ramirez's Ratings">
                Rebecca Ramirez
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/languages" title="View Hunter College High School's Languages Teachers">
                Languages
               </a>
              </div>
              <div class="teacher_actions" data-name="Rebecca Ramirez" data-sid="25767" data-status="-2" data-tid="1638618" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.2 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 92.400px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               33 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               She's pretty chill and nice but I don't think she knows everyone's names very well... and it's like by January you...
              </div>
              <div class="options">
               <a alt="View Rebecca Ramirez's Ratings" class="btn view_more" href="/rebecca-ramirez/1638618-t" title="View Rebecca Ramirez's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/rebecca-ramirez/1638618-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Richard Roundy's Ratings" class="name" href="/richard-roundy/224414-t" target="_blank" title="View Richard Roundy's Ratings">
                Richard Roundy
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/english" title="View Hunter College High School's English Teachers">
                English
               </a>
              </div>
              <div class="teacher_actions" data-name="Richard Roundy" data-sid="25767" data-status="-2" data-tid="224414" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.8 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 106.260px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               63 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               good teacher great sense of humor
              </div>
              <div class="options">
               <a alt="View Richard Roundy's Ratings" class="btn view_more" href="/richard-roundy/224414-t" title="View Richard Roundy's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/richard-roundy/224414-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Tara Foley's Ratings" class="name" href="/tara-foley/1714190-t" target="_blank" title="View Tara Foley's Ratings">
                Tara Foley
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/english" title="View Hunter College High School's English Teachers">
                English
               </a>
              </div>
              <div class="teacher_actions" data-name="Tara Foley" data-sid="25767" data-status="-2" data-tid="1714190" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.4 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 97.460px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               7 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               She's got he grammar down well. If you just make an effort to get to know her, she's an awesome person. Talk to her...
              </div>
              <div class="options">
               <a alt="View Tara Foley's Ratings" class="btn view_more" href="/tara-foley/1714190-t" title="View Tara Foley's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/tara-foley/1714190-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Hal Weinstein's Ratings" class="name" href="/hal-weinstein/316663-t" target="_blank" title="View Hal Weinstein's Ratings">
                Hal Weinstein
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/math" title="View Hunter College High School's Math Teachers">
                Math
               </a>
              </div>
              <div class="teacher_actions" data-name="Hal Weinstein" data-sid="25767" data-status="-2" data-tid="316663" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 87.560px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               47 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               I had him for seventh grade math last year, and I had a blast. He takes time with each new unit or concept to...
              </div>
              <div class="options">
               <a alt="View Hal Weinstein's Ratings" class="btn view_more" href="/hal-weinstein/316663-t" title="View Hal Weinstein's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/hal-weinstein/316663-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Rachel Basker's Ratings" class="name" href="/rachel-basker/246734-t" target="_blank" title="View Rachel Basker's Ratings">
                Rachel Basker
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/science" title="View Hunter College High School's Science Teachers">
                Science
               </a>
              </div>
              <div class="teacher_actions" data-name="Rachel Basker" data-sid="25767" data-status="-2" data-tid="246734" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="2.8 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 61.380px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               29 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               Her accent is horrible. Her teaching is horrible. I've done all of the stupid sheets that she gives me but.. no...
              </div>
              <div class="options">
               <a alt="View Rachel Basker's Ratings" class="btn view_more" href="/rachel-basker/246734-t" title="View Rachel Basker's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/rachel-basker/246734-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Christina Moore's Ratings" class="name" href="/christina-moore/1032723-t" target="_blank" title="View Christina Moore's Ratings">
                Christina Moore
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/math" title="View Hunter College High School's Math Teachers">
                Math
               </a>
              </div>
              <div class="teacher_actions" data-name="Christina Moore" data-sid="25767" data-status="-2" data-tid="1032723" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.3 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 95.260px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               23 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               she just tells us the stuff and doesn't explain it. She is only funny to the kids that get the best grades she is...
              </div>
              <div class="options">
               <a alt="View Christina Moore's Ratings" class="btn view_more" href="/christina-moore/1032723-t" title="View Christina Moore's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/christina-moore/1032723-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Ann Slavin's Ratings" class="name" href="/ann-slavin/242978-t" target="_blank" title="View Ann Slavin's Ratings">
                Ann Slavin
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/languages" title="View Hunter College High School's Languages Teachers">
                Languages
               </a>
              </div>
              <div class="teacher_actions" data-name="Ann Slavin" data-sid="25767" data-status="-2" data-tid="242978" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="3.4 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 73.920px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               51 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               am i crazy for preferring slavin to ramirez? though slavin may have favorites, she doesn't make it painfully obvious...
              </div>
              <div class="options">
               <a alt="View Ann Slavin's Ratings" class="btn view_more" href="/ann-slavin/242978-t" title="View Ann Slavin's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/ann-slavin/242978-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Johnson Wong's Ratings" class="name" href="/johnson-wong/1479620-t" target="_blank" title="View Johnson Wong's Ratings">
                Johnson Wong
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/physical-education" title="View Hunter College High School's Physical Education Teachers">
                Physical Education
               </a>
              </div>
              <div class="teacher_actions" data-name="Johnson Wong" data-sid="25767" data-status="-2" data-tid="1479620" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.5 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 98.340px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               25 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               COACH WONG!!! &lt;3 He was my ms volleyball coach for two years and I absolutely adore him! I think he could've been...
              </div>
              <div class="options">
               <a alt="View Johnson Wong's Ratings" class="btn view_more" href="/johnson-wong/1479620-t" title="View Johnson Wong's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/johnson-wong/1479620-t">
             </a>
            </div>
            <div class="placements" style="border: 1px solid transparent;">
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Julie Reifer's Ratings" class="name" href="/julie-reifer/239002-t" target="_blank" title="View Julie Reifer's Ratings">
                Julie Reifer
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/visual-arts" title="View Hunter College High School's Visual Arts Teachers">
                Visual Arts
               </a>
              </div>
              <div class="teacher_actions" data-name="Julie Reifer" data-sid="25767" data-status="-2" data-tid="239002" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 88.440px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               18 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               an actual good art teacher. with her, i retain info because the tests didn't make me memorize dates and unnecessary...
              </div>
              <div class="options">
               <a alt="View Julie Reifer's Ratings" class="btn view_more" href="/julie-reifer/239002-t" title="View Julie Reifer's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/julie-reifer/239002-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Joanne Roque's Ratings" class="name" href="/joanne-roque/246855-t" target="_blank" title="View Joanne Roque's Ratings">
                Joanne Roque
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/physics" title="View Hunter College High School's Physics Teachers">
                Physics
               </a>
              </div>
              <div class="teacher_actions" data-name="Joanne Roque" data-sid="25767" data-status="-2" data-tid="246855" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 87.560px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               25 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               She's definitely a kind and understanding teacher, and her exams are predictable and fair. But as a student whose...
              </div>
              <div class="options">
               <a alt="View Joanne Roque's Ratings" class="btn view_more" href="/joanne-roque/246855-t" title="View Joanne Roque's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/joanne-roque/246855-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Sewell's Ratings" class="name" href="/sewell/1054170-t" target="_blank" title="View Sewell's Ratings">
                Mrs. Sewell
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/science" title="View Hunter College High School's Science Teachers">
                Science
               </a>
              </div>
              <div class="teacher_actions" data-name="Mrs. Sewell" data-sid="25767" data-status="-2" data-tid="1054170" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.3 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 95.260px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               21 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               MS SEWELL YOU'RE AWESOME!!!!
              </div>
              <div class="options">
               <a alt="View Sewell's Ratings" class="btn view_more" href="/sewell/1054170-t" title="View Sewell's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/sewell/1054170-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Jose Diaz's Ratings" class="name" href="/jose-diaz/234507-t" target="_blank" title="View Jose Diaz's Ratings">
                Jose Diaz
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/languages" title="View Hunter College High School's Languages Teachers">
                Languages
               </a>
              </div>
              <div class="teacher_actions" data-name="Jose Diaz" data-sid="25767" data-status="-2" data-tid="234507" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.6 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 100.760px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               74 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               Best foreign language teacher I ever had. He could always make me laugh, and I learned a lot.
              </div>
              <div class="options">
               <a alt="View Jose Diaz's Ratings" class="btn view_more" href="/jose-diaz/234507-t" title="View Jose Diaz's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/jose-diaz/234507-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Melanie Pflaum's Ratings" class="name" href="/melanie-pflaum/1723216-t" target="_blank" title="View Melanie Pflaum's Ratings">
                Melanie Pflaum
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/math" title="View Hunter College High School's Math Teachers">
                Math
               </a>
              </div>
              <div class="teacher_actions" data-name="Melanie Pflaum" data-sid="25767" data-status="-2" data-tid="1723216" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.4 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 95.700px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               16 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               She is the best teacher ever.
              </div>
              <div class="options">
               <a alt="View Melanie Pflaum's Ratings" class="btn view_more" href="/melanie-pflaum/1723216-t" title="View Melanie Pflaum's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/melanie-pflaum/1723216-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Evanthia Basias' Ratings" class="name" href="/evanthia-basias/246866-t" target="_blank" title="View Evanthia Basias' Ratings">
                Evanthia Basias
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/math" title="View Hunter College High School's Math Teachers">
                Math
               </a>
              </div>
              <div class="teacher_actions" data-name="Evanthia Basias" data-sid="25767" data-status="-2" data-tid="246866" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.7 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 102.520px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               60 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               hands down the best math teacher i have ever had
              </div>
              <div class="options">
               <a alt="View Evanthia Basias' Ratings" class="btn view_more" href="/evanthia-basias/246866-t" title="View Evanthia Basias' Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/evanthia-basias/246866-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Shannon Connors' Ratings" class="name" href="/shannon-connors/1888882-t" target="_blank" title="View Shannon Connors' Ratings">
                Shannon Connors
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/math" title="View Hunter College High School's Math Teachers">
                Math
               </a>
              </div>
              <div class="teacher_actions" data-name="Shannon Connors" data-sid="25767" data-status="-2" data-tid="1888882" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.2 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 91.960px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               17 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               miss her so much! saw her profile on this page, and just couldn't resist. she was such an awesome explainer, and made...
              </div>
              <div class="options">
               <a alt="View Shannon Connors' Ratings" class="btn view_more" href="/shannon-connors/1888882-t" title="View Shannon Connors' Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/shannon-connors/1888882-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Shawn Crouch's Ratings" class="name" href="/shawn-crouch/240689-t" target="_blank" title="View Shawn Crouch's Ratings">
                Shawn Crouch
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/music" title="View Hunter College High School's Music Teachers">
                Music
               </a>
              </div>
              <div class="teacher_actions" data-name="Shawn Crouch" data-sid="25767" data-status="-2" data-tid="240689" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="3.7 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 82.280px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               51 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               His class is really easy. He kept saying that class participation was like 50% of your grade, but i only spoke twice...
              </div>
              <div class="options">
               <a alt="View Shawn Crouch's Ratings" class="btn view_more" href="/shawn-crouch/240689-t" title="View Shawn Crouch's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/shawn-crouch/240689-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Neil Potter's Ratings" class="name" href="/neil-potter/259598-t" target="_blank" title="View Neil Potter's Ratings">
                Neil Potter
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/physical-education" title="View Hunter College High School's Physical Education Teachers">
                Physical Education
               </a>
              </div>
              <div class="teacher_actions" data-name="Neil Potter" data-sid="25767" data-status="-2" data-tid="259598" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.6 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 102.080px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               14 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               Coach Potter is amazing! I met him through volleyball and even though he didnt really know me in seventh grade,...
              </div>
              <div class="options">
               <a alt="View Neil Potter's Ratings" class="btn view_more" href="/neil-potter/259598-t" title="View Neil Potter's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/neil-potter/259598-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Asumana Randolph's Ratings" class="name" href="/asumana-randolph/284663-t" target="_blank" title="View Asumana Randolph's Ratings">
                Asumana Randolph
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/science" title="View Hunter College High School's Science Teachers">
                Science
               </a>
              </div>
              <div class="teacher_actions" data-name="Asumana Randolph" data-sid="25767" data-status="-2" data-tid="284663" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.9 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 108.020px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               29 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               UGLYYYYYY ;)
He is literally the best. No words.
              </div>
              <div class="options">
               <a alt="View Asumana Randolph's Ratings" class="btn view_more" href="/asumana-randolph/284663-t" title="View Asumana Randolph's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/asumana-randolph/284663-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Gilana Reiss' Ratings" class="name" href="/gilana-reiss/1895207-t" target="_blank" title="View Gilana Reiss' Ratings">
                Gilana Reiss
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/chemistry" title="View Hunter College High School's Chemistry Teachers">
                Chemistry
               </a>
              </div>
              <div class="teacher_actions" data-name="Gilana Reiss" data-sid="25767" data-status="-2" data-tid="1895207" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.6 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 100.540px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               25 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               Ms. Reiss' Organic Chemistry Course was the best class I have taken at Hunter, and I am not a science kid. Ms. Reiss...
              </div>
              <div class="options">
               <a alt="View Gilana Reiss' Ratings" class="btn view_more" href="/gilana-reiss/1895207-t" title="View Gilana Reiss' Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/gilana-reiss/1895207-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Justin Storer's Ratings" class="name" href="/justin-storer/1901835-t" target="_blank" title="View Justin Storer's Ratings">
                Justin Storer
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/math" title="View Hunter College High School's Math Teachers">
                Math
               </a>
              </div>
              <div class="teacher_actions" data-name="Justin Storer" data-sid="25767" data-status="-2" data-tid="1901835" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.5 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 99.000px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               12 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               He is awesome. Enough said. Read the previous comments.
              </div>
              <div class="options">
               <a alt="View Justin Storer's Ratings" class="btn view_more" href="/justin-storer/1901835-t" title="View Justin Storer's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/justin-storer/1901835-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Kimberly Airoldi's Ratings" class="name" href="/kimberly-airoldi/229532-t" target="_blank" title="View Kimberly Airoldi's Ratings">
                Kimberly Airoldi
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/english" title="View Hunter College High School's English Teachers">
                English
               </a>
              </div>
              <div class="teacher_actions" data-name="Kimberly Airoldi" data-sid="25767" data-status="-2" data-tid="229532" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.4 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 97.680px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               49 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               She's actually amazing! She has a great sense of humor and always knows when to lighten up the discussion. She is a...
              </div>
              <div class="options">
               <a alt="View Kimberly Airoldi's Ratings" class="btn view_more" href="/kimberly-airoldi/229532-t" title="View Kimberly Airoldi's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/kimberly-airoldi/229532-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Sue Monroe's Ratings" class="name" href="/sue-monroe/317823-t" target="_blank" title="View Sue Monroe's Ratings">
                Sue Monroe
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/science" title="View Hunter College High School's Science Teachers">
                Science
               </a>
              </div>
              <div class="teacher_actions" data-name="Sue Monroe" data-sid="25767" data-status="-2" data-tid="317823" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="2.7 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 58.300px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               32 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               You'll think she's terrible in the beginning of the school year, then realize that you're actually somehow learning...
              </div>
              <div class="options">
               <a alt="View Sue Monroe's Ratings" class="btn view_more" href="/sue-monroe/317823-t" title="View Sue Monroe's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/sue-monroe/317823-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Emily Mines' Ratings" class="name" href="/emily-mines/7138025-t" target="_blank" title="View Emily Mines' Ratings">
                Emily Mines
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/math" title="View Hunter College High School's Math Teachers">
                Math
               </a>
              </div>
              <div class="teacher_actions" data-name="Emily Mines" data-sid="25767" data-status="-2" data-tid="7138025" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="3.6 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 78.980px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               9 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               I heard from other's that she's really mean and abrasive, which she can be at times, but overall is wonderful and...
              </div>
              <div class="options">
               <a alt="View Emily Mines' Ratings" class="btn view_more" href="/emily-mines/7138025-t" title="View Emily Mines' Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/emily-mines/7138025-t">
             </a>
            </div>
            <div class="placements" style="border: 1px solid transparent;">
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Inalni Sharma's Ratings" class="name" href="/inalni-sharma/2406390-t" target="_blank" title="View Inalni Sharma's Ratings">
                Inalni Sharma
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/chemistry" title="View Hunter College High School's Chemistry Teachers">
                Chemistry
               </a>
              </div>
              <div class="teacher_actions" data-name="Inalni Sharma" data-sid="25767" data-status="-2" data-tid="2406390" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.4 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 97.680px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               9 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               I LOVE THIS WOMAN!!! Also y'all dumb you misspelled her name. It's Mrinalni.
              </div>
              <div class="options">
               <a alt="View Inalni Sharma's Ratings" class="btn view_more" href="/inalni-sharma/2406390-t" title="View Inalni Sharma's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/inalni-sharma/2406390-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Lois Refkin's Ratings" class="name" href="/lois-refkin/242625-t" target="_blank" title="View Lois Refkin's Ratings">
                Lois Refkin
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/english" title="View Hunter College High School's English Teachers">
                English
               </a>
              </div>
              <div class="teacher_actions" data-name="Lois Refkin" data-sid="25767" data-status="-2" data-tid="242625" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.7 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 102.740px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               16 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               Ms. Refkin is the best English teacher I have ever met. She can be kind of funny at some times but she also knows...
              </div>
              <div class="options">
               <a alt="View Lois Refkin's Ratings" class="btn view_more" href="/lois-refkin/242625-t" title="View Lois Refkin's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/lois-refkin/242625-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Elaine Schwartz's Ratings" class="name" href="/elaine-schwartz/225812-t" target="_blank" title="View Elaine Schwartz's Ratings">
                Elaine Schwartz
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/science" title="View Hunter College High School's Science Teachers">
                Science
               </a>
              </div>
              <div class="teacher_actions" data-name="Elaine Schwartz" data-sid="25767" data-status="-2" data-tid="225812" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 88.220px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               31 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               I had her last year for 9th grade bio, and while she teaches off of her pptx, her tests are easy enough that you can...
              </div>
              <div class="options">
               <a alt="View Elaine Schwartz's Ratings" class="btn view_more" href="/elaine-schwartz/225812-t" title="View Elaine Schwartz's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/elaine-schwartz/225812-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Steve Young's Ratings" class="name" href="/steve-young/1906178-t" target="_blank" title="View Steve Young's Ratings">
                Steve Young
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/math-social-studies" title="View Hunter College High School's Math/Social Studies Teachers">
                Math/Social Studies
               </a>
              </div>
              <div class="teacher_actions" data-name="Steve Young" data-sid="25767" data-status="-2" data-tid="1906178" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.6 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 100.980px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               22 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               I had him for comp sci and he's fantastic. He expects you to read the book, since it's actually the key to doing well...
              </div>
              <div class="options">
               <a alt="View Steve Young's Ratings" class="btn view_more" href="/steve-young/1906178-t" title="View Steve Young's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/steve-young/1906178-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Sonya Mosco's Ratings" class="name" href="/sonya-mosco/240827-t" target="_blank" title="View Sonya Mosco's Ratings">
                Sonya Mosco
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/administration" title="View Hunter College High School's Administration Teachers">
                Administration
               </a>
              </div>
              <div class="teacher_actions" data-name="Sonya Mosco" data-sid="25767" data-status="-2" data-tid="240827" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.5 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 99.000px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               30 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               I was reluctant to post a comment on this rating site because it is normally a forum for people with grudges. Ms....
              </div>
              <div class="options">
               <a alt="View Sonya Mosco's Ratings" class="btn view_more" href="/sonya-mosco/240827-t" title="View Sonya Mosco's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/sonya-mosco/240827-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Yael Wyner's Ratings" class="name" href="/yael-wyner/172356-t" target="_blank" title="View Yael Wyner's Ratings">
                Yael Wyner
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/science" title="View Hunter College High School's Science Teachers">
                Science
               </a>
              </div>
              <div class="teacher_actions" data-name="Yael Wyner" data-sid="25767" data-status="-2" data-tid="172356" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="3.9 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 85.580px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               22 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               enough with the favorites. she doesn't like missbehaving. she and ms. fogleman are the best in the department.
              </div>
              <div class="options">
               <a alt="View Yael Wyner's Ratings" class="btn view_more" href="/yael-wyner/172356-t" title="View Yael Wyner's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/yael-wyner/172356-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Giovanna Termini's Ratings" class="name" href="/giovanna-termini/193565-t" target="_blank" title="View Giovanna Termini's Ratings">
                Giovanna Termini
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/social-studies" title="View Hunter College High School's Social Studies Teachers">
                Social Studies
               </a>
              </div>
              <div class="teacher_actions" data-name="Giovanna Termini" data-sid="25767" data-status="-2" data-tid="193565" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.3 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 95.260px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               73 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               She's a nice person and is always really cheery. But I hated her class so much because I was confused literally very...
              </div>
              <div class="options">
               <a alt="View Giovanna Termini's Ratings" class="btn view_more" href="/giovanna-termini/193565-t" title="View Giovanna Termini's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/giovanna-termini/193565-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Lori Jean D'Amico's Ratings" class="name" href="/lori-jean-d-amico/172360-t" target="_blank" title="View Lori Jean D'Amico's Ratings">
                Lori Jean D'Amico
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/english" title="View Hunter College High School's English Teachers">
                English
               </a>
              </div>
              <div class="teacher_actions" data-name="Lori Jean D'Amico" data-sid="25767" data-status="-2" data-tid="172360" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.4 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 96.140px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               79 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               I had Ms. D'Amico in 7th grade, and she was, by far, my favorite teacher. She taught very clearly and was always...
              </div>
              <div class="options">
               <a alt="View Lori Jean D'Amico's Ratings" class="btn view_more" href="/lori-jean-d-amico/172360-t" title="View Lori Jean D'Amico's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/lori-jean-d-amico/172360-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Richard Sasso's Ratings" class="name" href="/richard-sasso/246652-t" target="_blank" title="View Richard Sasso's Ratings">
                Richard Sasso
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/math" title="View Hunter College High School's Math Teachers">
                Math
               </a>
              </div>
              <div class="teacher_actions" data-name="Richard Sasso" data-sid="25767" data-status="-2" data-tid="246652" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="3.3 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 71.500px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               34 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               He is a good teacher but he insults his students way to much.
              </div>
              <div class="options">
               <a alt="View Richard Sasso's Ratings" class="btn view_more" href="/richard-sasso/246652-t" title="View Richard Sasso's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/richard-sasso/246652-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Daniel Mozes' Ratings" class="name" href="/daniel-mozes/1922357-t" target="_blank" title="View Daniel Mozes' Ratings">
                Daniel Mozes
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/english" title="View Hunter College High School's English Teachers">
                English
               </a>
              </div>
              <div class="teacher_actions" data-name="Daniel Mozes" data-sid="25767" data-status="-2" data-tid="1922357" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.8 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 104.720px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               30 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               Dr. Mozes is really chill and one of the funniest teachers I've ever had. He genuinely wants EVERYONE in his class to...
              </div>
              <div class="options">
               <a alt="View Daniel Mozes' Ratings" class="btn view_more" href="/daniel-mozes/1922357-t" title="View Daniel Mozes' Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/daniel-mozes/1922357-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Michelle Rushforth's Ratings" class="name" href="/michelle-rushforth/1923892-t" target="_blank" title="View Michelle Rushforth's Ratings">
                Michelle Rushforth
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/health" title="View Hunter College High School's Health Teachers">
                Health
               </a>
              </div>
              <div class="teacher_actions" data-name="Michelle Rushforth" data-sid="25767" data-status="-2" data-tid="1923892" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.3 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 95.480px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               18 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               super chill class, i've done so much of my other hw in it and she sees and doesn't care (although it might be because...
              </div>
              <div class="options">
               <a alt="View Michelle Rushforth's Ratings" class="btn view_more" href="/michelle-rushforth/1923892-t" title="View Michelle Rushforth's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/michelle-rushforth/1923892-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Sandra Miley's Ratings" class="name" href="/sandra-miley/262028-t" target="_blank" title="View Sandra Miley's Ratings">
                Sandra Miley
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/physical-education" title="View Hunter College High School's Physical Education Teachers">
                Physical Education
               </a>
              </div>
              <div class="teacher_actions" data-name="Sandra Miley" data-sid="25767" data-status="-2" data-tid="262028" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="3.8 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 82.940px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               26 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               Ms. Miley was the rock of our 1982-3 undefeated volleyball team. She united a group of young women from very diverse...
              </div>
              <div class="options">
               <a alt="View Sandra Miley's Ratings" class="btn view_more" href="/sandra-miley/262028-t" title="View Sandra Miley's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/sandra-miley/262028-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Philip Frankel's Ratings" class="name" href="/philip-frankel/1875164-t" target="_blank" title="View Philip Frankel's Ratings">
                Philip Frankel
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/science" title="View Hunter College High School's Science Teachers">
                Science
               </a>
              </div>
              <div class="teacher_actions" data-name="Philip Frankel" data-sid="25767" data-status="-2" data-tid="1875164" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.9 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 107.360px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               19 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               Mr. Frankel is a great and funny teacher who understands and explains everything. I really enjoyed having him as my...
              </div>
              <div class="options">
               <a alt="View Philip Frankel's Ratings" class="btn view_more" href="/philip-frankel/1875164-t" title="View Philip Frankel's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/philip-frankel/1875164-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Lee Weinberg's Ratings" class="name" href="/lee-weinberg/337869-t" target="_blank" title="View Lee Weinberg's Ratings">
                Lee Weinberg
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/counselor" title="View Hunter College High School's Counselor Teachers">
                Counselor
               </a>
              </div>
              <div class="teacher_actions" data-name="Lee Weinberg" data-sid="25767" data-status="-2" data-tid="337869" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="3.7 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 81.180px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               22 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               She's very helpful and really cares about the students. Shes also super nice and doesnt mind if you just pop in.
              </div>
              <div class="options">
               <a alt="View Lee Weinberg's Ratings" class="btn view_more" href="/lee-weinberg/337869-t" title="View Lee Weinberg's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/lee-weinberg/337869-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Eugene Lim's Ratings" class="name" href="/eugene-lim/1998685-t" target="_blank" title="View Eugene Lim's Ratings">
                Eugene Lim
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/librarian" title="View Hunter College High School's Librarian Teachers">
                Librarian
               </a>
              </div>
              <div class="teacher_actions" data-name="Eugene Lim" data-sid="25767" data-status="-2" data-tid="1998685" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="5.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 108.900px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               13 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               Mr. Lim and Mrs. Seigmann
are right to tell you you're wrong
              </div>
              <div class="options">
               <a alt="View Eugene Lim's Ratings" class="btn view_more" href="/eugene-lim/1998685-t" title="View Eugene Lim's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/eugene-lim/1998685-t">
             </a>
            </div>
            <div class="placements" style="border: 1px solid transparent;">
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Melinda Stepanski's Ratings" class="name" href="/melinda-stepanski/1845470-t" target="_blank" title="View Melinda Stepanski's Ratings">
                Melinda Stepanski
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/english" title="View Hunter College High School's English Teachers">
                English
               </a>
              </div>
              <div class="teacher_actions" data-name="Melinda Stepanski" data-sid="25767" data-status="-2" data-tid="1845470" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="3.1 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 67.100px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               10 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               I've learned a lot from Ms. Stepanski, she encourages and inspires those of us who want to really learn. You may...
              </div>
              <div class="options">
               <a alt="View Melinda Stepanski's Ratings" class="btn view_more" href="/melinda-stepanski/1845470-t" title="View Melinda Stepanski's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/melinda-stepanski/1845470-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Pamela Lewis' Ratings" class="name" href="/pamela-lewis/172355-t" target="_blank" title="View Pamela Lewis' Ratings">
                Pamela Lewis
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/languages" title="View Hunter College High School's Languages Teachers">
                Languages
               </a>
              </div>
              <div class="teacher_actions" data-name="Pamela Lewis" data-sid="25767" data-status="-2" data-tid="172355" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="3.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 65.120px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               46 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               She usually knows what she's talking about, but she definitely picks favorites. I learned a lot from her class, but...
              </div>
              <div class="options">
               <a alt="View Pamela Lewis' Ratings" class="btn view_more" href="/pamela-lewis/172355-t" title="View Pamela Lewis' Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/pamela-lewis/172355-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Anthony Natelli's Ratings" class="name" href="/anthony-natelli/1960538-t" target="_blank" title="View Anthony Natelli's Ratings">
                Anthony Natelli
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/counselor" title="View Hunter College High School's Counselor Teachers">
                Counselor
               </a>
              </div>
              <div class="teacher_actions" data-name="Anthony Natelli" data-sid="25767" data-status="-2" data-tid="1960538" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.8 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 106.260px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               3 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               I liked Natelli. He's not great with abstract questions ("Where should I apply?"), but if you come to him with a...
              </div>
              <div class="options">
               <a alt="View Anthony Natelli's Ratings" class="btn view_more" href="/anthony-natelli/1960538-t" title="View Anthony Natelli's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/anthony-natelli/1960538-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Wallace's Ratings" class="name" href="/wallace/239035-t" target="_blank" title="View Wallace's Ratings">
                Mr. Wallace
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/substitute-teacher" title="View Hunter College High School's Substitute Teacher Teachers">
                Substitute Teacher
               </a>
              </div>
              <div class="teacher_actions" data-name="Mr. Wallace" data-sid="25767" data-status="-2" data-tid="239035" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="3.4 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 73.920px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               35 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               Had her as a sub TWICE. She said "the Wallace is back" and proceeded to glare at my entire class the second day. Rude...
              </div>
              <div class="options">
               <a alt="View Wallace's Ratings" class="btn view_more" href="/wallace/239035-t" title="View Wallace's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/wallace/239035-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Carolyn Mayadas' Ratings" class="name" href="/carolyn-mayadas/264965-t" target="_blank" title="View Carolyn Mayadas' Ratings">
                Carolyn Mayadas
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/computer-science" title="View Hunter College High School's Computer Science Teachers">
                Computer Science
               </a>
              </div>
              <div class="teacher_actions" data-name="Carolyn Mayadas" data-sid="25767" data-status="-2" data-tid="264965" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.4 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 97.240px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               4 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               The best ever couldn't get any better!!!!!!!:)
              </div>
              <div class="options">
               <a alt="View Carolyn Mayadas' Ratings" class="btn view_more" href="/carolyn-mayadas/264965-t" title="View Carolyn Mayadas' Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/carolyn-mayadas/264965-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Bob Sabin's Ratings" class="name" href="/bob-sabin/962015-t" target="_blank" title="View Bob Sabin's Ratings">
                Bob Sabin
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/music" title="View Hunter College High School's Music Teachers">
                Music
               </a>
              </div>
              <div class="teacher_actions" data-name="Bob Sabin" data-sid="25767" data-status="-2" data-tid="962015" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.6 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 100.100px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               19 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               Best teacher Ive ever had. So understanding and so helpful and you learn so much in his class. Love him.
              </div>
              <div class="options">
               <a alt="View Bob Sabin's Ratings" class="btn view_more" href="/bob-sabin/962015-t" title="View Bob Sabin's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/bob-sabin/962015-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Howard Adams' Ratings" class="name" href="/howard-adams/2074712-t" target="_blank" title="View Howard Adams' Ratings">
                Howard Adams
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/physical-education" title="View Hunter College High School's Physical Education Teachers">
                Physical Education
               </a>
              </div>
              <div class="teacher_actions" data-name="Howard Adams" data-sid="25767" data-status="-2" data-tid="2074712" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="4.4 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 96.140px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               10 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               Howard Adams is the best coach ever!!!!!!!!!!!!!!!!!!!!!!
              </div>
              <div class="options">
               <a alt="View Howard Adams' Ratings" class="btn view_more" href="/howard-adams/2074712-t" title="View Howard Adams' Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/howard-adams/2074712-t">
             </a>
            </div>
            <div class="clickable_fix row teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Eve Eisenstadt's Ratings" class="name" href="/eve-eisenstadt/246828-t" target="_blank" title="View Eve Eisenstadt's Ratings">
                Eve Eisenstadt
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/visual-arts" title="View Hunter College High School's Visual Arts Teachers">
                Visual Arts
               </a>
              </div>
              <div class="teacher_actions" data-name="Eve Eisenstadt" data-sid="25767" data-status="-2" data-tid="246828" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="3.8 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 84.480px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               16 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               she is such a bad teacher she doesnt teach anything just sits and eats food and has her student teacher teach and...
              </div>
              <div class="options">
               <a alt="View Eve Eisenstadt's Ratings" class="btn view_more" href="/eve-eisenstadt/246828-t" title="View Eve Eisenstadt's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/eve-eisenstadt/246828-t">
             </a>
            </div>
            <div class="clickable_fix row secondary teacher">
             <div class="col-xs-3 info">
              <h3 class="teacher_name">
               <a alt="View Kelly Honerkamp's Ratings" class="name" href="/kelly-honerkamp/7898685-t" target="_blank" title="View Kelly Honerkamp's Ratings">
                Kelly Honerkamp
               </a>
              </h3>
              <div class="department">
               Department
               <a href="/hunter-college-high-school/25767-s/math" title="View Hunter College High School's Math Teachers">
                Math
               </a>
              </div>
              <div class="teacher_actions" data-name="Kelly Honerkamp" data-sid="25767" data-status="-2" data-tid="7898685" style="display:none;">
              </div>
             </div>
             <div class="col-xs-2 col-lg-3 score">
              <div class="rateit star-rating rateit-exclude" title="2.0 of 5">
               <div class="rateit-range" style="width: 110px; height: 18px;">
                <div class="rateit-preset rateit-selected" style="height: 18px; width: 43.120px;">
                </div>
               </div>
              </div>
              <div class="rating_count">
               9 ratings
              </div>
             </div>
             <div class="col-xs-7 col-lg-6 comments">
              Recent Rating
              <div class="comment_extract">
               Ms. Honerkamp is hilarious and really smart. Honestly, she's an awesome teacher. However, I never do too well on her...
              </div>
              <div class="options">
               <a alt="View Kelly Honerkamp's Ratings" class="btn view_more" href="/kelly-honerkamp/7898685-t" title="View Kelly Honerkamp's Ratings">
                View More
                <i class="fa fa-angle-right">
                </i>
               </a>
              </div>
             </div>
             <a class="clickable_fix_trigger hidden-sm hidden-md hidden-lg" href="/kelly-honerkamp/7898685-t">
             </a>
            </div>
           </div>
           <div class="row pagination_container">
            <div class="text">
             Page
1
of
3
            </div>
            <ul class="pagination">
             <li class="page active">
              <a href="/hunter-college-high-school/25767-s" title="Page 1">
               1
              </a>
             </li>
             <li class="page">
              <a href="/hunter-college-high-school/25767-s/2" rel="next" title="Next Page">
               2
              </a>
             </li>
             <li class="page">
              <a href="/hunter-college-high-school/25767-s/3" title="Page 3">
               3
              </a>
             </li>
             <li class="next_page">
              <a href="/hunter-college-high-school/25767-s/2" rel="next" title="Next Page">
               <span class="hidden-sm hidden-md hidden-lg">
                <i class="fa fa-chevron-right">
                </i>
               </span>
               <span class="hidden-xs">
                <i class="fa fa-long-arrow-right">
                </i>
               </span>
              </a>
             </li>
             <li class="last_page">
              <a href="/hunter-college-high-school/25767-s/3" title="Last Page">
               <span class="hidden-sm hidden-md hidden-lg">
                <i class="fa fa-chevron-right">
                </i>
                <i class="fa fa-chevron-right">
                </i>
               </span>
               <span class="hidden-xs">
                <i class="fa fa-angle-double-right">
                </i>
               </span>
              </a>
             </li>
            </ul>
           </div>
          </div>
         </div>
         <div class="col-xs-12 col-lg-3 secondary_column">
          <div class="ad_container ATF_rectangle sponsor">
           <div id="School_ATF_Rectangle">
            <div class="ad-tag" data-ad-name="halfpage_Desktop_mrec" data-ad-size="300x250">
            </div>
           </div>
          </div>
          <a class="rating_histogram_widget_link_container" href="/hunter-college-high-school/25767-s/stats" title="Go to Hunter College High School stats">
           <div class="row block_container school_rating_histogram_card">
            <div class="col-xs-12">
             <h2 class="school_name" title="Learn more about Hunter College High School">
              <span>
               Hunter College High School Rating Histogram
              </span>
             </h2>
             <div class="score_line_container">
              <div class="score_label">
               5-star
              </div>
              <div class="score_percentage">
               69%
              </div>
              <div class="score_line">
               <div class="aux" style="width: 69.61%;">
               </div>
              </div>
             </div>
             <div class="score_line_container">
              <div class="score_label">
               4-star
              </div>
              <div class="score_percentage">
               14%
              </div>
              <div class="score_line">
               <div class="aux" style="width: 14.1%;">
               </div>
              </div>
             </div>
             <div class="score_line_container">
              <div class="score_label">
               3-star
              </div>
              <div class="score_percentage">
               8%
              </div>
              <div class="score_line">
               <div class="aux" style="width: 8.49%;">
               </div>
              </div>
             </div>
             <div class="score_line_container">
              <div class="score_label">
               2-star
              </div>
              <div class="score_percentage">
               2%
              </div>
              <div class="score_line">
               <div class="aux" style="width: 2.89%;">
               </div>
              </div>
             </div>
             <div class="score_line_container">
              <div class="score_label">
               1-star
              </div>
              <div class="score_percentage">
               4%
              </div>
              <div class="score_line">
               <div class="aux" style="width: 4.9%;">
               </div>
              </div>
             </div>
             <div class="score">
              <div class="rateit star-rating rateit-exclude" title="4.0 of 5">
               <div class="rateit-range" style="width: 90px; height: 15px;">
                <div class="rateit-preset rateit-selected" style="height: 15px; width: 71.517px;">
                </div>
               </div>
              </div>
              <span class="rating-summary">
               Based on
4,301
Ratings
              </span>
             </div>
            </div>
           </div>
          </a>
          <div class="sticky_container_right">
           <div class="sticky_column">
            <div class="ad_container ATF_rectangle_2">
             <div class="sponsor">
              <div style="min-height:250px; width:300px;">
               <div class="ad-tag" data-ad-name="mrec_desktop_2" data-ad-size="300x250" id="mrec_desktop_2">
               </div>
              </div>
             </div>
            </div>
           </div>
          </div>
         </div>
        </div>
       </section>
      </div>
     </div>
    </div>
   </div>
  </div>
  <div id="all_footer_wrapper" style="overflow:hidden;">
   <section class="container-fluid hidden-xs padding" id="states">
    <div class="container">
     <div class="row">
      <div class="col-xs-12 col-sm-12 col-sm-offset-0 footer_states_container">
       <h3>
        Locate Schools by State:
       </h3>
       <div class="states">
        <div class="state">
         <a alt="Find Alaska's High Schools and Colleges" href="/alaska" title="Find Alaska's High Schools and Colleges">
          Alaska
         </a>
        </div>
        <div class="state">
         <a alt="Find Alabama's High Schools and Colleges" href="/alabama" title="Find Alabama's High Schools and Colleges">
          Alabama
         </a>
        </div>
        <div class="state">
         <a alt="Find Arkansas' High Schools and Colleges" href="/arkansas" title="Find Arkansas' High Schools and Colleges">
          Arkansas
         </a>
        </div>
        <div class="state">
         <a alt="Find Arizona's High Schools and Colleges" href="/arizona" title="Find Arizona's High Schools and Colleges">
          Arizona
         </a>
        </div>
        <div class="state">
         <a alt="Find California's High Schools and Colleges" href="/california" title="Find California's High Schools and Colleges">
          California
         </a>
        </div>
        <div class="state">
         <a alt="Find Colorado's High Schools and Colleges" href="/colorado" title="Find Colorado's High Schools and Colleges">
          Colorado
         </a>
        </div>
        <div class="state">
         <a alt="Find Connecticut's High Schools and Colleges" href="/connecticut" title="Find Connecticut's High Schools and Colleges">
          Connecticut
         </a>
        </div>
        <div class="state">
         <a alt="Find DC's High Schools and Colleges" href="/dc" title="Find DC's High Schools and Colleges">
          DC
         </a>
        </div>
        <div class="state">
         <a alt="Find Delaware's High Schools and Colleges" href="/delaware" title="Find Delaware's High Schools and Colleges">
          Delaware
         </a>
        </div>
        <div class="state">
         <a alt="Find Florida's High Schools and Colleges" href="/florida" title="Find Florida's High Schools and Colleges">
          Florida
         </a>
        </div>
        <div class="state">
         <a alt="Find Georgia's High Schools and Colleges" href="/georgia" title="Find Georgia's High Schools and Colleges">
          Georgia
         </a>
        </div>
        <div class="state">
         <a alt="Find Hawaii's High Schools and Colleges" href="/hawaii" title="Find Hawaii's High Schools and Colleges">
          Hawaii
         </a>
        </div>
        <div class="state">
         <a alt="Find Iowa's High Schools and Colleges" href="/iowa" title="Find Iowa's High Schools and Colleges">
          Iowa
         </a>
        </div>
        <div class="state">
         <a alt="Find Idaho's High Schools and Colleges" href="/idaho" title="Find Idaho's High Schools and Colleges">
          Idaho
         </a>
        </div>
        <div class="state">
         <a alt="Find Illinois' High Schools and Colleges" href="/illinois" title="Find Illinois' High Schools and Colleges">
          Illinois
         </a>
        </div>
        <div class="state">
         <a alt="Find Indiana's High Schools and Colleges" href="/indiana" title="Find Indiana's High Schools and Colleges">
          Indiana
         </a>
        </div>
        <div class="state">
         <a alt="Find Kansas' High Schools and Colleges" href="/kansas" title="Find Kansas' High Schools and Colleges">
          Kansas
         </a>
        </div>
        <div class="state">
         <a alt="Find Kentucky's High Schools and Colleges" href="/kentucky" title="Find Kentucky's High Schools and Colleges">
          Kentucky
         </a>
        </div>
        <div class="state">
         <a alt="Find Louisiana's High Schools and Colleges" href="/louisiana" title="Find Louisiana's High Schools and Colleges">
          Louisiana
         </a>
        </div>
        <div class="state">
         <a alt="Find Massachusetts' High Schools and Colleges" href="/massachusetts" title="Find Massachusetts' High Schools and Colleges">
          Massachusetts
         </a>
        </div>
        <div class="state">
         <a alt="Find Maryland's High Schools and Colleges" href="/maryland" title="Find Maryland's High Schools and Colleges">
          Maryland
         </a>
        </div>
        <div class="state">
         <a alt="Find Maine's High Schools and Colleges" href="/maine" title="Find Maine's High Schools and Colleges">
          Maine
         </a>
        </div>
        <div class="state">
         <a alt="Find Michigan's High Schools and Colleges" href="/michigan" title="Find Michigan's High Schools and Colleges">
          Michigan
         </a>
        </div>
        <div class="state">
         <a alt="Find Minnesota's High Schools and Colleges" href="/minnesota" title="Find Minnesota's High Schools and Colleges">
          Minnesota
         </a>
        </div>
        <div class="state">
         <a alt="Find Missouri's High Schools and Colleges" href="/missouri" title="Find Missouri's High Schools and Colleges">
          Missouri
         </a>
        </div>
        <div class="state">
         <a alt="Find Mississippi's High Schools and Colleges" href="/mississippi" title="Find Mississippi's High Schools and Colleges">
          Mississippi
         </a>
        </div>
        <div class="state">
         <a alt="Find Montana's High Schools and Colleges" href="/montana" title="Find Montana's High Schools and Colleges">
          Montana
         </a>
        </div>
        <div class="state">
         <a alt="Find North Carolina's High Schools and Colleges" href="/north-carolina" title="Find North Carolina's High Schools and Colleges">
          North Carolina
         </a>
        </div>
        <div class="state">
         <a alt="Find North Dakota's High Schools and Colleges" href="/north-dakota" title="Find North Dakota's High Schools and Colleges">
          North Dakota
         </a>
        </div>
        <div class="state">
         <a alt="Find Nebraska's High Schools and Colleges" href="/nebraska" title="Find Nebraska's High Schools and Colleges">
          Nebraska
         </a>
        </div>
        <div class="state">
         <a alt="Find New Hampshire's High Schools and Colleges" href="/new-hampshire" title="Find New Hampshire's High Schools and Colleges">
          New Hampshire
         </a>
        </div>
        <div class="state">
         <a alt="Find New Jersey's High Schools and Colleges" href="/new-jersey" title="Find New Jersey's High Schools and Colleges">
          New Jersey
         </a>
        </div>
        <div class="state">
         <a alt="Find New Mexico's High Schools and Colleges" href="/new-mexico" title="Find New Mexico's High Schools and Colleges">
          New Mexico
         </a>
        </div>
        <div class="state">
         <a alt="Find Nevada's High Schools and Colleges" href="/nevada" title="Find Nevada's High Schools and Colleges">
          Nevada
         </a>
        </div>
        <div class="state">
         <a alt="Find New York's High Schools and Colleges" href="/new-york" title="Find New York's High Schools and Colleges">
          New York
         </a>
        </div>
        <div class="state">
         <a alt="Find Ohio's High Schools and Colleges" href="/ohio" title="Find Ohio's High Schools and Colleges">
          Ohio
         </a>
        </div>
        <div class="state">
         <a alt="Find Oklahoma's High Schools and Colleges" href="/oklahoma" title="Find Oklahoma's High Schools and Colleges">
          Oklahoma
         </a>
        </div>
        <div class="state">
         <a alt="Find Oregon's High Schools and Colleges" href="/oregon" title="Find Oregon's High Schools and Colleges">
          Oregon
         </a>
        </div>
        <div class="state">
         <a alt="Find Pennsylvania's High Schools and Colleges" href="/pennsylvania" title="Find Pennsylvania's High Schools and Colleges">
          Pennsylvania
         </a>
        </div>
        <div class="state">
         <a alt="Find Puerto Rico's High Schools and Colleges" href="/puerto-rico" title="Find Puerto Rico's High Schools and Colleges">
          Puerto Rico
         </a>
        </div>
        <div class="state">
         <a alt="Find Rhode Island's High Schools and Colleges" href="/rhode-island" title="Find Rhode Island's High Schools and Colleges">
          Rhode Island
         </a>
        </div>
        <div class="state">
         <a alt="Find South Carolina's High Schools and Colleges" href="/south-carolina" title="Find South Carolina's High Schools and Colleges">
          South Carolina
         </a>
        </div>
        <div class="state">
         <a alt="Find South Dakota's High Schools and Colleges" href="/south-dakota" title="Find South Dakota's High Schools and Colleges">
          South Dakota
         </a>
        </div>
        <div class="state">
         <a alt="Find Tennessee's High Schools and Colleges" href="/tennessee" title="Find Tennessee's High Schools and Colleges">
          Tennessee
         </a>
        </div>
        <div class="state">
         <a alt="Find Texas' High Schools and Colleges" href="/texas" title="Find Texas' High Schools and Colleges">
          Texas
         </a>
        </div>
        <div class="state">
         <a alt="Find Utah's High Schools and Colleges" href="/utah" title="Find Utah's High Schools and Colleges">
          Utah
         </a>
        </div>
        <div class="state">
         <a alt="Find Virginia's High Schools and Colleges" href="/virginia" title="Find Virginia's High Schools and Colleges">
          Virginia
         </a>
        </div>
        <div class="state">
         <a alt="Find Vermont's High Schools and Colleges" href="/vermont" title="Find Vermont's High Schools and Colleges">
          Vermont
         </a>
        </div>
        <div class="state">
         <a alt="Find Washington's High Schools and Colleges" href="/washington" title="Find Washington's High Schools and Colleges">
          Washington
         </a>
        </div>
        <div class="state">
         <a alt="Find Wisconsin's High Schools and Colleges" href="/wisconsin" title="Find Wisconsin's High Schools and Colleges">
          Wisconsin
         </a>
        </div>
        <div class="state">
         <a alt="Find West Virginia's High Schools and Colleges" href="/west-virginia" title="Find West Virginia's High Schools and Colleges">
          West Virginia
         </a>
        </div>
        <div class="state">
         <a alt="Find Wyoming's High Schools and Colleges" href="/wyoming" title="Find Wyoming's High Schools and Colleges">
          Wyoming
         </a>
        </div>
       </div>
      </div>
     </div>
    </div>
   </section>
   <section class="container-fluid" id="footer_directory">
    <div class="container">
     <div class="row">
      <div class="col-xs-6 hidden-xs">
       High School and College Directory:
       <a alt='Schools beginning with "A"' href="/schools/directory/a" title='Schools beginning with "A"'>
        a
       </a>
       <a alt='Schools beginning with "B"' href="/schools/directory/b" title='Schools beginning with "B"'>
        b
       </a>
       <a alt='Schools beginning with "C"' href="/schools/directory/c" title='Schools beginning with "C"'>
        c
       </a>
       <a alt='Schools beginning with "D"' href="/schools/directory/d" title='Schools beginning with "D"'>
        d
       </a>
       <a alt='Schools beginning with "E"' href="/schools/directory/e" title='Schools beginning with "E"'>
        e
       </a>
       <a alt='Schools beginning with "F"' href="/schools/directory/f" title='Schools beginning with "F"'>
        f
       </a>
       <a alt='Schools beginning with "G"' href="/schools/directory/g" title='Schools beginning with "G"'>
        g
       </a>
       <a alt='Schools beginning with "H"' href="/schools/directory/h" title='Schools beginning with "H"'>
        h
       </a>
       <a alt='Schools beginning with "I"' href="/schools/directory/i" title='Schools beginning with "I"'>
        i
       </a>
       <a alt='Schools beginning with "J"' href="/schools/directory/j" title='Schools beginning with "J"'>
        j
       </a>
       <a alt='Schools beginning with "K"' href="/schools/directory/k" title='Schools beginning with "K"'>
        k
       </a>
       <a alt='Schools beginning with "L"' href="/schools/directory/l" title='Schools beginning with "L"'>
        l
       </a>
       <a alt='Schools beginning with "M"' href="/schools/directory/m" title='Schools beginning with "M"'>
        m
       </a>
       <a alt='Schools beginning with "N"' href="/schools/directory/n" title='Schools beginning with "N"'>
        n
       </a>
       <a alt='Schools beginning with "O"' href="/schools/directory/o" title='Schools beginning with "O"'>
        o
       </a>
       <a alt='Schools beginning with "P"' href="/schools/directory/p" title='Schools beginning with "P"'>
        p
       </a>
       <a alt='Schools beginning with "Q"' href="/schools/directory/q" title='Schools beginning with "Q"'>
        q
       </a>
       <a alt='Schools beginning with "R"' href="/schools/directory/r" title='Schools beginning with "R"'>
        r
       </a>
       <a alt='Schools beginning with "S"' href="/schools/directory/s" title='Schools beginning with "S"'>
        s
       </a>
       <a alt='Schools beginning with "T"' href="/schools/directory/t" title='Schools beginning with "T"'>
        t
       </a>
       <a alt='Schools beginning with "U"' href="/schools/directory/u" title='Schools beginning with "U"'>
        u
       </a>
       <a alt='Schools beginning with "V"' href="/schools/directory/v" title='Schools beginning with "V"'>
        v
       </a>
       <a alt='Schools beginning with "W"' href="/schools/directory/w" title='Schools beginning with "W"'>
        w
       </a>
       <a alt='Schools beginning with "X"' href="/schools/directory/x" title='Schools beginning with "X"'>
        x
       </a>
       <a alt='Schools beginning with "Y"' href="/schools/directory/y" title='Schools beginning with "Y"'>
        y
       </a>
       <a alt='Schools beginning with "Z"' href="/schools/directory/z" title='Schools beginning with "Z"'>
        z
       </a>
       <a alt="Schools beginning with numbers" href="/schools/directory/%23" title="Schools beginning with numbers">
        #
       </a>
      </div>
      <div class="col-xs-6 hidden-xs">
       Teacher and Professor Directory:
       <a alt='Teachers beginning with "A"' href="/teachers/directory/a" title='Teachers beginning with "A"'>
        a
       </a>
       <a alt='Teachers beginning with "B"' href="/teachers/directory/b" title='Teachers beginning with "B"'>
        b
       </a>
       <a alt='Teachers beginning with "C"' href="/teachers/directory/c" title='Teachers beginning with "C"'>
        c
       </a>
       <a alt='Teachers beginning with "D"' href="/teachers/directory/d" title='Teachers beginning with "D"'>
        d
       </a>
       <a alt='Teachers beginning with "E"' href="/teachers/directory/e" title='Teachers beginning with "E"'>
        e
       </a>
       <a alt='Teachers beginning with "F"' href="/teachers/directory/f" title='Teachers beginning with "F"'>
        f
       </a>
       <a alt='Teachers beginning with "G"' href="/teachers/directory/g" title='Teachers beginning with "G"'>
        g
       </a>
       <a alt='Teachers beginning with "H"' href="/teachers/directory/h" title='Teachers beginning with "H"'>
        h
       </a>
       <a alt='Teachers beginning with "I"' href="/teachers/directory/i" title='Teachers beginning with "I"'>
        i
       </a>
       <a alt='Teachers beginning with "J"' href="/teachers/directory/j" title='Teachers beginning with "J"'>
        j
       </a>
       <a alt='Teachers beginning with "K"' href="/teachers/directory/k" title='Teachers beginning with "K"'>
        k
       </a>
       <a alt='Teachers beginning with "L"' href="/teachers/directory/l" title='Teachers beginning with "L"'>
        l
       </a>
       <a alt='Teachers beginning with "M"' href="/teachers/directory/m" title='Teachers beginning with "M"'>
        m
       </a>
       <a alt='Teachers beginning with "N"' href="/teachers/directory/n" title='Teachers beginning with "N"'>
        n
       </a>
       <a alt='Teachers beginning with "O"' href="/teachers/directory/o" title='Teachers beginning with "O"'>
        o
       </a>
       <a alt='Teachers beginning with "P"' href="/teachers/directory/p" title='Teachers beginning with "P"'>
        p
       </a>
       <a alt='Teachers beginning with "Q"' href="/teachers/directory/q" title='Teachers beginning with "Q"'>
        q
       </a>
       <a alt='Teachers beginning with "R"' href="/teachers/directory/r" title='Teachers beginning with "R"'>
        r
       </a>
       <a alt='Teachers beginning with "S"' href="/teachers/directory/s" title='Teachers beginning with "S"'>
        s
       </a>
       <a alt='Teachers beginning with "T"' href="/teachers/directory/t" title='Teachers beginning with "T"'>
        t
       </a>
       <a alt='Teachers beginning with "U"' href="/teachers/directory/u" title='Teachers beginning with "U"'>
        u
       </a>
       <a alt='Teachers beginning with "V"' href="/teachers/directory/v" title='Teachers beginning with "V"'>
        v
       </a>
       <a alt='Teachers beginning with "W"' href="/teachers/directory/w" title='Teachers beginning with "W"'>
        w
       </a>
       <a alt='Teachers beginning with "X"' href="/teachers/directory/x" title='Teachers beginning with "X"'>
        x
       </a>
       <a alt='Teachers beginning with "Y"' href="/teachers/directory/y" title='Teachers beginning with "Y"'>
        y
       </a>
       <a alt='Teachers beginning with "Z"' href="/teachers/directory/z" title='Teachers beginning with "Z"'>
        z
       </a>
      </div>
     </div>
     <div class="row footer_countries_list">
      <div class="col-xs-10 col-xs-offset-1 col-sm-12 col-sm-offset-0">
       RateMyTeachers International:
       <a alt="United States" class="country" href="https://www.ratemyteachers.com" title="United States">
        United States
       </a>
       <a alt="Canada" class="country" href="https://ca.ratemyteachers.com" title="Canada">
        Canada
       </a>
       <a alt="United Kingdom" class="country" href="https://uk.ratemyteachers.com" title="United Kingdom">
        United Kingdom
       </a>
       <a alt="Australia" class="country" href="https://au.ratemyteachers.com" title="Australia">
        Australia
       </a>
       <a alt="New Zealand" class="country" href="https://nz.ratemyteachers.com" title="New Zealand">
        New Zealand
       </a>
       <a alt="Ireland" class="country" href="https://ie.ratemyteachers.com" title="Ireland">
        Ireland
       </a>
      </div>
     </div>
    </div>
   </section>
   <section class="container-fluid" id="footer">
    <div class="container">
     <div class="row footer_links">
      <div class="col-xs-10 col-xs-offset-1 col-sm-12 col-sm-offset-0">
       <h3 class="hidden-sm hidden-md hidden-lg">
        Quick Links
       </h3>
       <ul>
        <li>
         <a alt="RateMyTeachers Frequently Asked Questions" href="/faq" title="RateMyTeachers Frequently Asked Questions">
          FAQ
         </a>
        </li>
        <li>
         <a data-backdrop="static" data-keyboard="" data-remote="/contact/new" data-target="#modal" data-toggle="modal" href="javascript:void(0);" rel="nofollow" title="Contact RateMyTeachers">
          Contact
         </a>
        </li>
        <li>
         <a href="/terms" title="RateMyTeachers Terms of Use">
          Terms of Use
         </a>
        </li>
        <li>
         <a alt="RateMyTeachers Privacy Policy" href="/privacy" title="RateMyTeachers Privacy Policy">
          Privacy Policy
         </a>
        </li>
        <li>
         <a href="/site-guidelines" title="RateMyTeachers Site Guidelines">
          Site Guidelines
         </a>
        </li>
        <li>
         <a href="/copyright" title="RateMyTeachers Copyright Compliance">
          Copyright Compliance
         </a>
        </li>
       </ul>
      </div>
     </div>
     <div class="row copyright">
      Copyright 2001-2018 RateMyTeachers.com. All Rights Reserved.
     </div>
    </div>
   </section>
   <div aria-hidden="true" class="modal fade" id="modal" role="dialog" style="width: auto;" tabindex="-1">
    <div class="modal-dialog">
     <div class="modal-content">
     </div>
    </div>
   </div>
   <div aria-hidden="true" class="modal fade" id="modal_rating" role="dialog" style="width: auto;" tabindex="-1">
    <div class="modal-dialog">
     <div class="modal-content">
     </div>
    </div>
   </div>
   <div id="loading-indicator" style="display: none;">
    <div>
     Please wait...
     <br/>
     <img alt="Ajax loader" src="/assets/ajax-loader-e483da860d5177651d2a88eda6a66b00.gif"/>
    </div>
   </div>
   <div class="amp_ad_unit amp_ad_unit_template" style="display: none;">
    <a class="amp_clickurl amp_no_text" href="javascript:void(0);" rel="nofollow" target="_blank">
     <span class="amp_title">
     </span>
     <span class="amp_extension_merchant_rating" style="display: none;">
      <span class="amp_extension_merchant_rating_rating" data-star-width="18">
       <div class="rateit star-rating rateit-exclude" title="">
        <div class="rateit-range" style="width: 90px; height: 15px;">
         <div class="rateit-preset rateit-selected" style="height: 15px; width: 0.000px;">
         </div>
        </div>
       </div>
      </span>
     </span>
     <span class="amp_description">
     </span>
     <span class="amp_displayurl">
     </span>
     <img class="amp_impressionurl" style="height: 1px; width: 1px;"/>
    </a>
    <span class="row amp_extension_site_links">
    </span>
    <span class="arrow">
     <span class="aux">
     </span>
    </span>
    <span class="amp_site_link_template" style="display: none;">
     <a class="col-xs-6 amp_extension_site_links_link">
      <span class="amp_extension_site_links_text">
      </span>
     </a>
    </span>
   </div>
  </div>
  <script type="text/javascript">
   functionToLoad.push('//ajax.googleapis.com/ajax/libs/jqueryui/1.11.2/jquery-ui.min.js');
  </script>
  <script type="text/javascript">
   functionToLoad.push('/assets/application-b341b3f30de53e073ed952dffffa800f.js');
    functionToLoad.push('/assets/users-816a475ba77b361e679d83227c475c2f.js');
  </script>
  <script type="text/javascript">
   functionToLoad.push(function() {
        // Facebook like
        // (function(d, s, id) {
        //   var js, fjs = d.getElementsByTagName(s)[0];
        //   if (d.getElementById(id)) return;
        //   js = d.createElement(s); js.id = id;
        //   js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&appId=232453153516852&version=v2.0";
        //   fjs.parentNode.insertBefore(js, fjs);
        // }(document, 'script', 'facebook-jssdk'));

        // Google Plus
        // (function() {
        //   var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true;
        //   po.src = 'https://apis.google.com/js/platform.js';
        //   var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);
        // })();

        // Twitter Follow
        // !function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src="//platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");

      });
  </script>
  <script>
   functionToLoad.push(function() {
    $('#teachers_by_alphabet').change(function(e){
      document.location.href = $('#teachers_by_alphabet').val()
    });
  });
  </script>
  <script>
   functionToLoad.push(function() {
    var schoolPagePath = '/hunter-college-high-school/25767-s';
    var resultCount = 100;
    var minStickyResultCount = 3;

    if (!isMobile && !isMedium && resultCount > 0) {
      var stickyColumnRight = $(".sticky_container_right .sticky_column");
      var stickyColumnCenter = $(".sticky_container_center .sticky_column");
      var footerHeight = $('#all_footer_wrapper').outerHeight() + 50;
      var stickyOptions = function(getWidthFrom) {
        return {topSpacing:0, getWidthFrom: getWidthFrom, responsiveWidth: true, bottomSpacing: footerHeight};
      }
      stickyColumnRight.sticky(stickyOptions('.sticky_container_right'));

      // Make center column options sticky when min results quantity
      if (resultCount > minStickyResultCount - 1) {
        stickyColumnCenter.sticky(stickyOptions('.sticky_container_center', 0));
      }
    }
  });
  </script>
  <script type="text/javascript">
   // AMP_ADS Bottom
        functionToLoad.push([function() {
          var bottomUrl = 'https://ratemyteachers_contextual.ampfeed.com/xmlamp/feed?deco=1&extn=0%2C2&ip=66.108.83.14&partner=ratemyteachers_contextual&qt=%5B%22online+colleges+in+New+York%22%5D&results=4&rfr=https%3A%2F%2Fwww.ratemyteachers.com%2Fhunter-college-high-school%2F25767-s&sub1=Desktop&sub2=School&ua=python-requests%2F2.18.4&v=5';
          ampAdRegister('amp_ads_bottom', bottomUrl, "amp_ad_school_unit_template");
        }, true]);
  </script>
  <div class="amp_ad_unit amp_ad_school_unit_template" style="display: none;">
   <a class="amp_clickurl amp_no_text" href="javascript:void(0);" rel="nofollow" target="_blank">
    <span class="amp_title">
    </span>
    <span class="amp_displayurl">
    </span>
    <span class="amp_extension_merchant_rating" style="display: none;">
     <span class="amp_extension_merchant_rating_rating" data-star-width="18">
      <div class="rateit star-rating rateit-exclude" title="">
       <div class="rateit-range" style="width: 90px; height: 15px;">
        <div class="rateit-preset rateit-selected" style="height: 15px; width: 0.000px;">
        </div>
       </div>
      </div>
     </span>
    </span>
    <span class="amp_description">
    </span>
    <img class="amp_impressionurl" style="height: 1px; width: 1px;"/>
   </a>
   <span class="row amp_extension_site_links">
   </span>
   <span class="arrow">
    <span class="aux">
    </span>
   </span>
   <span class="amp_site_link_template" style="display: none;">
    <a class="col-xs-6 amp_extension_site_links_link">
     <span class="amp_extension_site_links_text">
     </span>
    </a>
   </span>
  </div>
  <script type="text/javascript">
   function initializeMaps() {
      var length = mapFunctionArray.length;
      for (var i = 0; i < length; i++) {
        mapFunctionArray[i]();
      }
    }

    functionToLoad.push(function() {
      // Don't load google maps when no pending maps
      if (typeof(mapFunctionArray) === 'undefined' || mapFunctionArray.length < 1)
        return;

      var googleMapsId = "AIzaSyDQOhmnZnwlz7TM334xnTn4JByjjxEgq1g";

      var script_path = "https://maps.googleapis.com/maps/api/js?key=" + googleMapsId + "&sensor=false&callback=initializeMaps";
      $.getScript(script_path);

    });
  </script>
  <script type="text/javascript">
   functionToLoad.push(function() {
        $('.search_form input[name=q]').on("autocompleteopen", function(e) {
          var input = $(e.target);
          var url = 'https://ratemyteachers_contextual.ampfeed.com/xmlamp/feed?deco=1&extn=0%2C2&ip=66.108.83.14&partner=ratemyteachers_contextual&results=2&rfr=https%3A%2F%2Fwww.ratemyteachers.com%2Fhunter-college-high-school%2F25767-s&sub1=desktop&sub2=searchbox&ua=python-requests%2F2.18.4&v=5';
          var country = 'United States';
          var location = '';
          var keywords = 'online colleges in ';
          if ($('#state').val() !== '') {
            location = $("#state option:selected").text();
            location = location.split('-')[0];
            //keywords = 'online colleges in ';
          } else {
            location = country;
            //keywords = 'online colleges in ';
          }
          url += '&qt=["' + encodeURIComponent(keywords + location) + '"]';
          ampAdRegister('amp_ads_autocomplete', url);
        });
      });
  </script>
  <script>
   window.addEventListener('load', function(){
      console.info("[PERF] DomContentLoaded: " + ((new Date()).getTime() - window.beginTimeTrack));
    });

    window.addEventListener('load', function(){
      console.info("[PERF] Load: " + ((new Date()).getTime() - window.beginTimeTrack));
    });
  </script>
  <script type="text/javascript">
   (function() {
      // Load script from url
      var loadScript = function(url, callback) {
        var script = document.createElement("script");
        script.type = "text/javascript";

        // Add on load callback event
        if (callback !== null) {
          if (script.readyState){ //IE
            script.onreadystatechange = function(){
              if (script.readyState == "loaded" || script.readyState == "complete"){
                script.onreadystatechange = null;
                callback();
              }
            };
          } else { //Others
            // Execute callback even when an error happen
            script.onerror = function(e){
              try {
                console.error("An error happen when loading '" + err.target.src + "' script.");
              } catch(err) {} finally {
                callback();
              }
            };
            script.onload = function(){ callback(); };
          }
        }

        // Load the script
        script.src = url;
        document.body.appendChild(script);
      };

      // Load scripts in a sequence instead parallel
      // to make sure frameworks load correctly
      function sequence(index, max, source) {
        if (index < max) {
          var data = functionToLoad.extractElementData(source[index]);

          if (typeof data.element === 'string') {
            if (data.async) {
              // Async script
              loadScript(data.element, function() {
                if (data.subElements.length > 0) {
                  sequence(0, data.subElements.length, data.subElements);
                }
              });
              sequence(index + 1, max, source);
            } else {
              // Sync scripts
              loadScript(data.element, function() {
                if (data.subElements.length > 0) {
                  sequence(0, data.subElements.length, data.subElements);
                }
                sequence(index + 1, max, source);
              });
            }
          } else {
            // Execute callback even when an error happen on the function
            try {
              if (data.async) {
                // Async script
                setTimeout(function() { data.element(); }, 1);
              } else {
                // Sync script
                data.element();
              }
            } catch(err) {
              console.error(err);
            } finally {
              sequence(index + 1, max, source);
            }
          }
        }
      }

      // Load all javascript in a sequence
      var loadDeferredJs = function() {
        sequence(0, functionToLoad.length, functionToLoad);
      };

      // Execute all lazy javascripts after DOM load
      var raf = requestAnimationFrame || mozRequestAnimationFrame ||
          webkitRequestAnimationFrame || msRequestAnimationFrame;
      if (raf) raf(function() { window.setTimeout(loadDeferredJs, 0); });
      else window.addEventListener('load', loadDeferredJs);
    })();
  </script>
 </body>
</html>