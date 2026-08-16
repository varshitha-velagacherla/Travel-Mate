from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights



res=search_flights("plan a 7days Japan Trip from Bangladesh")
print(res)

#res=tavily_search("Best Hotels in India")
#print(res)