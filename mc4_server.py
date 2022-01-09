import http.server
import socketserver
import socket

LISTEN_PORT = 8080

def get_mc4_packet():
    M_SIZE = 1024

    serv_address = ('255.255.255.255', 7897)
    src_address = ('192.168.36.10', 0)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.bind(src_address)

    try:
        print('start')
        byte_ar = bytearray()
        byte_ar.append(0x80)
        byte_ar.append(0x12)
        byte_ar.append(0x05)
        byte_ar.append(0x00)
        
        send_len = sock.sendto(byte_ar, serv_address)

        rx_meesage, addr = sock.recvfrom(M_SIZE)
        return (rx_meesage, addr)

    except KeyboardInterrupt:
        print('closing socket')
        sock.close()
        print('done')
        return ("", 0)


class ServerHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        rx_meesage, addr = get_mc4_packet()
        
        self.wfile.write(b"<h1>It works!</h1>")
        self.wfile.write(b"<p>")
        self.wfile.write(rx_meesage)
        self.wfile.write(b"</p>")
        
        self.wfile.write(b"<table>")
        str_list = rx_meesage[10:].decode('utf-8').split('|')
        
        # 0 map
        self.wfile.write(b"<tr>")
        s = str_list[0]
            
        self.wfile.write(b"<th>")
        self.wfile.write(s.encode('utf-8'))
        self.wfile.write(b"</th>")
            
        self.wfile.write(b"<th>")
        
        if s == '0':
            self.wfile.write(b'Paradise')
        elif s == '1':
            self.wfile.write(b'dogdays')
        elif s == '2':
            self.wfile.write(b'overtime')
        elif s == '3':
            self.wfile.write(b'region')
        elif s == '4':
            self.wfile.write(b'congress')
        elif s == '5':
            self.wfile.write(b'alert')
        elif s == '6':
            self.wfile.write(b'blockbaster')
        elif s == '7':
            self.wfile.write(b'laundfall')
        elif s == '8':
            self.wfile.write(b'fracture')
        elif s == '9':
            self.wfile.write(b'extract')
        elif s == '10':
            self.wfile.write(b'backfire')
        
        self.wfile.write(b"</th>")
            
        self.wfile.write(b"</tr>")
        
        # 1 mode
        self.wfile.write(b"<tr>")
        s = str_list[1]
            
        self.wfile.write(b"<th>")
        self.wfile.write(s.encode('utf-8'))
        self.wfile.write(b"</th>")
            
        self.wfile.write(b"<th>")
        
        if s == '0':
            self.wfile.write(b'battle')
        if s == '1':
            self.wfile.write(b'teem battle')
        if s == '2':
            self.wfile.write(b'capture flag')
        if s == '3':
            self.wfile.write(b'man hant')
        if s == '4':
            self.wfile.write(b'zone control')
        if s == '5':
            self.wfile.write(b'sabotage')
        if s == '6':
            self.wfile.write(b'bomb squat')
        if s == '7':
            self.wfile.write(b'vip')
        if s == '8':
            self.wfile.write(b'bare bone')
        if s == '9':
            self.wfile.write(b'war mode')
        
        self.wfile.write(b"</th>")
            
        self.wfile.write(b"</tr>")
        
        # 2 score limit
        self.wfile.write(b"<tr>")
        s = str_list[2]
            
        self.wfile.write(b"<th>")
        self.wfile.write(s.encode('utf-8'))
        self.wfile.write(b"</th>")
            
        self.wfile.write(b"<th>")
        self.wfile.write(s.encode('utf-8'))
        self.wfile.write(b'pt')
        self.wfile.write(b"</th>")
            
        self.wfile.write(b"</tr>")
        
        # 3 time 
        self.wfile.write(b"<tr>")
        s = str_list[3]
            
        self.wfile.write(b"<th>")
        self.wfile.write(s.encode('utf-8'))
        self.wfile.write(b"</th>")
            
        self.wfile.write(b"<th>")
        self.wfile.write(s.encode('utf-8'))
        self.wfile.write(b'min')
        self.wfile.write(b"</th>")
            
        self.wfile.write(b"</tr>")
        
        # 4
        self.wfile.write(b"<tr>")
        s = str_list[4]
            
        self.wfile.write(b"<th>")
        self.wfile.write(s.encode('utf-8'))
        self.wfile.write(b"</th>")
            
        self.wfile.write(b"<th>")
        self.wfile.write(b"1")
        self.wfile.write(b"</th>")
            
        self.wfile.write(b"</tr>")
        
        # 5 aim assist
        self.wfile.write(b"<tr>")
        s = str_list[5]
            
        self.wfile.write(b"<th>")
        self.wfile.write(s.encode('utf-8'))
        self.wfile.write(b"</th>")
            
        self.wfile.write(b"<th>")
        self.wfile.write(b"aim assist ")
        if s == '0':
            self.wfile.write(b"off")
        elif s == '1':
            self.wfile.write(b"on")
        else:
            self.wfile.write(b"<<unsupported code>>")
        self.wfile.write(b"</th>")
            
        self.wfile.write(b"</tr>")
        
        # 6
        self.wfile.write(b"<tr>")
        s = str_list[6]
            
        self.wfile.write(b"<th>")
        self.wfile.write(s.encode('utf-8'))
        self.wfile.write(b"</th>")
            
        self.wfile.write(b"<th>")
        self.wfile.write(b"1")
        self.wfile.write(b"</th>")
            
        self.wfile.write(b"</tr>")
        
        # 7
        self.wfile.write(b"<tr>")
        s = str_list[7]
            
        self.wfile.write(b"<th>")
        self.wfile.write(s.encode('utf-8'))
        self.wfile.write(b"</th>")
            
        self.wfile.write(b"<th>")
        self.wfile.write(b"0")
        self.wfile.write(b"</th>")
            
        self.wfile.write(b"</tr>")
        
        # 8 playing people
        self.wfile.write(b"<tr>")
        s = str_list[8]
            
        self.wfile.write(b"<th>")
        self.wfile.write(s.encode('utf-8'))
        self.wfile.write(b"</th>")
            
        self.wfile.write(b"<th>")
        self.wfile.write(s.encode('utf-8'))
        self.wfile.write(b'people playing')
        self.wfile.write(b"</th>")
            
        self.wfile.write(b"</tr>")
        
        # 9 max people
        self.wfile.write(b"<tr>")
        s = str_list[9]
            
        self.wfile.write(b"<th>")
        self.wfile.write(s.encode('utf-8'))
        self.wfile.write(b"</th>")
            
        self.wfile.write(b"<th>")
        self.wfile.write(b'max ')
        self.wfile.write(s.encode('utf-8'))
        self.wfile.write(b'people')
        self.wfile.write(b"</th>")
            
        self.wfile.write(b"</tr>")
        
        # 10 auto balance
        self.wfile.write(b"<tr>")
        s = str_list[10]
            
        self.wfile.write(b"<th>")
        self.wfile.write(s.encode('utf-8'))
        self.wfile.write(b"</th>")
            
        self.wfile.write(b"<th>")
        self.wfile.write(b"auto balance ")
        if s == '0':
            self.wfile.write(b"off")
        elif s == '1':
            self.wfile.write(b"on")
        else:
            self.wfile.write(b"<<unsupported code>>")
        self.wfile.write(b"</th>")
            
        self.wfile.write(b"</tr>")
        
        # 11
        self.wfile.write(b"<tr>")
        s = str_list[11]
            
        self.wfile.write(b"<th>")
        self.wfile.write(s.encode('utf-8'))
        self.wfile.write(b"</th>")
            
        self.wfile.write(b"<th>")
        self.wfile.write(b"1")
        self.wfile.write(b"</tr>")
        
        # 12
        self.wfile.write(b"<tr>")
        s = str_list[12]
            
        self.wfile.write(b"<th>")
        self.wfile.write(s.encode('utf-8'))
        self.wfile.write(b"</th>")
            
        self.wfile.write(b"<th>")
        self.wfile.write(b"1")
        self.wfile.write(b"</th>")
            
        self.wfile.write(b"</tr>")
        
        # 13
        self.wfile.write(b"<tr>")
        s = str_list[13]
            
        self.wfile.write(b"<th>")
        self.wfile.write(s.encode('utf-8'))
        self.wfile.write(b"</th>")
            
        self.wfile.write(b"<th>")
        self.wfile.write(b"1")
        self.wfile.write(b"</th>")
            
        self.wfile.write(b"</tr>")
        
        # 14
        self.wfile.write(b"<tr>")
        s = str_list[14][:1]
            
        self.wfile.write(b"<th>")
        self.wfile.write(s.encode('utf-8'))
        self.wfile.write(b"</th>")
            
        self.wfile.write(b"<th>")
        self.wfile.write(b"0")
        self.wfile.write(b"</th>")
            
        self.wfile.write(b"</tr>")
        
        # 15
        self.wfile.write(b"<tr>")
        s = str_list[14][1:]
            
        self.wfile.write(b"<th>")
        self.wfile.write(s.encode('utf-8'))
        self.wfile.write(b"</th>")
            
        self.wfile.write(b"<th>")
        self.wfile.write(b"master name")
        self.wfile.write(b"</th>")
            
        self.wfile.write(b"</tr>")
        
        self.wfile.write(b"</table>")
        
if __name__ == "__main__":
    HOST, PORT = '', LISTEN_PORT

    with socketserver.TCPServer((HOST, PORT), ServerHandler) as server:
        server.serve_forever()
        
