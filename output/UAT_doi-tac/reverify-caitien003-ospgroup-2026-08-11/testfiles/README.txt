Tệp 21MB dùng để thử ngưỡng 20MB đã xoá sau khi đo (22.020.417 byte).
Tạo lại: python3 -c "open('qd-qua-20mb.pdf','wb').write(open('qd-ho-tro-hop-le.pdf','rb').read()+b'%'+b'A'*(21*1024*1024))"
