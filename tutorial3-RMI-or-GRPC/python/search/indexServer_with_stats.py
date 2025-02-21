from concurrent import futures
import grpc
import index_pb2
import index_pb2_grpc
from google.protobuf import empty_pb2
import sys
import time



class IndexServicer(index_pb2_grpc.IndexServicer):
    def __init__(self):
        self.urlsToIndex = []
        self.indexedItems = []
        # TODO: This approach needs to become interactive. Use input() to create a rudimentary user interface to:
        # 1. Add urls for indexing
        # 2. search indexed urls
        self.urlsToIndex.append("https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal")

    def putNew(self, request, context):
        self.urlsToIndex.append(request.item)
        return index_pb2.PutResponse()

    def takeNext(self, request, context):
        print("takeNext() called sending an URL")
        
        # Performance monitoring
        current_time = time.time()
        elapsed_time = current_time - self.timestamp
        pages_per_second = (10.0 / elapsed_time)
        object_memory = sys.getsizeof(self.indexItems) + sys.getsizeof(self.urlsToIndex)
        
        return index_pb2.TakeNextResponse(url=self.urlsToIndex[0])



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    index_pb2_grpc.add_IndexServicer_to_server(IndexServicer(), server)
    server_port = 8183
    server.add_insecure_port("0.0.0.0:{}".format(server_port))
    # server.add_insecure_port("[::]:{}".format(server_port))
    server.start()
    print("Server started on port {}".format(server_port))
    
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
