import ibm_db


try:
    print("Connecting...")
    conn = ibm_db.connect(
        "DATABASE=bludb;HOSTNAME=21fecfd8-47b7-4937-840d-d791d0218660.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31864;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;PROTOCOL=TCPIP;UID=jfs93288;PWD=7DLlZanU3kI83jSN;",
        "", "")
    server = ibm_db.server_info(conn)
    print(server.DBMS_NAME)
    print("Connected")
    stmt = ibm_db.exec_immediate(conn, "SELECT * FROM USERS")
    while ibm_db.fetch_row(stmt) != False:
        print(ibm_db.result(stmt, 0))
except:
    print("Can't connect")