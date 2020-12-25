#!/usr/bin/env python
from ast import literal_eval
from socket import *
import os
import uuid

s = socket(AF_INET, SOCK_STREAM)

s.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)

s.bind(('', 8080))

s.listen(1)

while 1:

        try:

                os.fork()

                c, addr = s.accept()

		# \r\n\r\n
                rsp_200 = '''HTTP/1.1 200 OK\r\n\Content-Type: text/html; charset=utf-8\r\n\Server: XFFF/2.7\r\n\r\n'''

		# \r\n one
                rsp_ses = '''HTTP/1.1 200 OK\r\n\Content-Type: text/html; charset=utf-8\r\n\Server: XFFF/2.7\r\n'''

		main = "3.3.3.3"

                location_href_login = "http://" + main + "/login"

		location_href_auth = "http://" + main + "/auth"

		location_href_main = "http://" + main

                data = c.recv(1024)

                data_h = data.split("\r\n")


                if data_h[0][:4] == "POST":

                        data_1 = data.split("\r\n\r\n")
                        # flag=test_1  ||  id=test&pw=pass

                        

                        if data_1[1][:2] == "id":

                                data_22 = data_1[1].split("&")
                                # ['id=test', 'pw=pass']

                                data_33 = data_22[0].split("=")
                                # ['id', 'test']

                                id = data_33[1]

                                data_44 = data_22[1].split("=")
                                # ['pw', 'pass']

                                pw = data_44[1]

                                ### id_db ###
                                f = open("../2_db/id.db","r")

                                id_db_pre = f.read()

                                f.close()

                                id_db = literal_eval(id_db_pre)

				# id_db[id] error
				try:


					
	                                if id_db[id] == pw:

        	                                #print id_db[id]

                	                        #print pw

	                                        f = open("../2_db/session.db","r")

        	                                ses_db = f.read()

                	                        f.close()

                        	                ses_db = literal_eval(ses_db)

                                	        session = uuid.uuid4()

                                        	ses_db[id] = session.hex

	                                        f = open("../2_db/session.db","w")

        	                                f.write(str(ses_db))

                	                        f.close()

                        	                rsp_ses += "Set-Cookie:XFFF=" + session.hex + "\r\n\r\n"

						
                                	        rsp_ses += '''<html><body><script>alert("Hello, ''' + id + '''");location.href="''' + location_href_login  + '''";</script></body></html>'''

                                        	c.send(rsp_ses)

					else:

	                                        rsp_200 += '''<html><body><script>alert("Wrong ID or PW");location.href="''' + location_href_login  + '''";</script></body></html>'''

        	                                c.send(rsp_200)

                                except:

                                        rsp_200 += '''<html><body><script>alert("Wrong ID or PW");location.href="''' + location_href_login  + '''";</script></body></html>'''

                                        c.send(rsp_200)




                        elif data_1[1][:4] == "flag":
				
				f = open("../2_db/session.db","r")

                                ses_db = f.read()

                                f.close()

                                ses_db = literal_eval(ses_db)

                                cok_check = "XFFF="

                                # { key : value } => { value : key }
                                rev_ses_db = {v: k for k, v in ses_db.items()}

                                for text in data_h:

                                        if cok_check in text:

                                                # text =>>>  Cookie: XFFF=session

                                                cok = text.split("=")
                                                #  Cookie: XFFF , session

                                                cok = cok[1]

                                                if len(cok) == 32:

                                                        pass

                                                else:

                                                 	c.send(rsp_200 + '''<html><body><script>alert("Plz login");location.href="''' + location_href_auth + '''";</script></body></html>''')
	     	            			        c.close()

						try:

                                                	if rev_ses_db[cok]:

								id = rev_ses_db[cok]

				                            	data_2 = data_1[1].split("=")
                        			        	flag = data_2[1]
	
								### flag_db[flag][chn] == info_id[id]

        	                			        ### flag_db ###
				                                f = open("../2_db/flag.db","r")
	
                	        			        flag_db = f.read()

				                                f.close()



								f = open("../2_db/info_id.db","r")
								info_id = f.read()

								f.close()


                        				        flag_db = literal_eval(flag_db)

								info_id = literal_eval(info_id)


								# for_2 <!-- flag -->
								if flag == "Gou5gcFbzGn3Bg9FsnuLYUaXBCByBdm6s21wrDM":

									c.send(rsp_200 + '''<html><body><script>alert("[NO CLEAR] Find real flag");/*0jLZOXEagqAyZ2HpgmNZBl81MzFHpHhbN9Qklfi*/location.href="''' + location_href_auth + '''";</script></body></html>''')

									c.close()

								else:

									pass



								try:


									if flag_db[flag]: 


										chn = flag_db[flag]["chn"]
			
										if info_id[id][chn] == 'n':

											info_id[id][chn] = "y"
	
			        				                        flag_msg = flag_db[flag]["msg"]

               	        						                flag_pt = flag_db[flag]["pt"]

											id_point = info_id[id]["pt"]
											id_point = int(id_point)
	
											id_point += int(flag_pt)

											info_id[id]["pt"] = str(id_point)

											f = open("../2_db/info_id.db","w")

											f.write(str(info_id))

											f.close()											

											c.send(rsp_200 + '''<html><body><script>alert("[CLEAR] ''' + flag_msg + '''   +''' + flag_pt + '''pt");location.href="''' + location_href_auth + '''";</script></body></html>''')
											c.close()


										else:

					        		                        flag_msg = flag_db[flag]["msg"]
	
											c.send(rsp_200 + '''<html><body><script>alert("[ALREADY] ''' + flag_msg + '''");location.href="''' + location_href_auth + '''";</script></body></html>''')

											c.close()

								except:

	                        	                         	c.send(rsp_200 + '''<html><body><script>alert("Wrong flag");location.href="''' + location_href_auth + '''";</script></body></html>''')
		     	            				        c.close()


			                        except:
							c.send(rsp_200 + '''<html><body><script>alert("Plz login");location.href="''' + location_href_auth + '''";</script></body></html>''')
        	            			        c.close()


					else:

						pass
				
				c.send(rsp_200 + '''<html><body><script>alert("Plz login");location.href="''' + location_href_auth + '''";</script></body></html>''')
         			c.close()



			else:

				c.send(rsp_200 + '''<html><body><script>location.href="''' + location_href_main + '''";</script></body></html>''')
		           	c.close()



                else:

			c.send(rsp_200 + '''<html><body><script>location.href="''' + location_href_main + '''";</script></body></html>''')
	           	c.close()


        except:

                pass
