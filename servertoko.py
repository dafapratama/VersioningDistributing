#import library server
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client

#Batasi hanya pada path /RPC2 saja supaya tidak bisa mengakses path lainnya
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)
    
# Buat server
with SimpleXMLRPCServer(('127.0.0.1', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()
#buat fungsi pilihan barang
    def milih(pilihan):
        if pilihan == 1:
            return 3000
        elif pilihan == 2:
            return 14000
        elif pilihan == 3:
            return 2000
        elif pilihan == 4:
            return 8000
        elif pilihan == 5:
            return 2500
        elif pilihan == 6:
            return 5000
        elif pilihan == 7:
            return 2500
        elif pilihan == 8:
            return 5000
        elif pilihan == 9:
            return 5000
        elif pilihan == 10:
            return 500
        else:
            return 0

    #fungsi hasil
    def Hasil(harga, jumlah_beli):
        return harga*jumlah_beli
    #fungsi kembalian
    def kembalian(bayar, total):
        return bayar-total;

    server.register_multicall_functions()
    server.register_function(Hasil, "hasil")
    server.register_function(kembalian, "kembalian")
    server.register_function(milih, "pilihan")
    server.serve_forever()

