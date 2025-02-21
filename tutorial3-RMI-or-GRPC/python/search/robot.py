import grpc
from google.protobuf import empty_pb2
import index_pb2
import index_pb2_grpc
import requests
from bs4 import BeautifulSoup as jsoup

def run():
    # Create a gRPC channel
    channel = grpc.insecure_channel('localhost:8183')
    
    # Create a stub (client)
    stub = index_pb2_grpc.IndexStub(channel)
    
    try:
        try:
            response = stub.takeNext(empty_pb2.Empty())
            print(response.url)
            url = response.url
            print(f"Received URL: {url}")
            
            try:
                # Fetch webpage using requests and parse with BeautifulSoup
                response = requests.get(url)
                response.raise_for_status()  # Raise an exception for bad status codes
                soup = jsoup(response.text, 'html.parser')
                print(soup)
                # TODO: Get all text and tokenize. 
                # TODO: find new URls and submit to queue

            except requests.RequestException as e:
                print(f"Error fetching webpage: {e}")
            
        except grpc.RpcError as e:
            print(f"RPC failed: {e.code()}")
            print(f"RPC error details: {e.details()}")
            raise
                
    except KeyboardInterrupt:
        print("\nStopping the robot...")
        
if __name__ == '__main__':
    run()
