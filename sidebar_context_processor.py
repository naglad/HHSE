# sidebar_context_processor.py
def sidebar_context(request):
    # Example: Fetching a query result
    query_result = "Your query result here"
    return {'query_result': query_result}