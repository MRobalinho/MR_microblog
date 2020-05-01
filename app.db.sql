BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "followers" (
	"follower_id"	INTEGER,
	"followed_id"	INTEGER,
	FOREIGN KEY("followed_id") REFERENCES "user"("id"),
	FOREIGN KEY("follower_id") REFERENCES "user"("id")
);
CREATE TABLE IF NOT EXISTS "post" (
	"id"	INTEGER NOT NULL,
	"body"	VARCHAR(140),
	"timestamp"	DATETIME,
	"user_id"	INTEGER,
	"language"	VARCHAR(5),
	PRIMARY KEY("id"),
	FOREIGN KEY("user_id") REFERENCES "user"("id")
);
CREATE TABLE IF NOT EXISTS "user" (
	"id"	INTEGER NOT NULL,
	"username"	VARCHAR(64),
	"email"	VARCHAR(120),
	"password_hash"	VARCHAR(128),
	"about_me"	VARCHAR(140),
	"last_seen"	DATETIME,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "alembic_version" (
	"version_num"	VARCHAR(32) NOT NULL,
	CONSTRAINT "alembic_version_pkc" PRIMARY KEY("version_num")
);
INSERT INTO "followers" VALUES (1,2);
INSERT INTO "followers" VALUES (1,5);
INSERT INTO "followers" VALUES (2,5);
INSERT INTO "followers" VALUES (2,3);
INSERT INTO "followers" VALUES (3,1);
INSERT INTO "followers" VALUES (3,4);
INSERT INTO "followers" VALUES (2,4);
INSERT INTO "post" VALUES (1,'Teste msg Susan','2020-04-11 16:46:20.399568',1,NULL);
INSERT INTO "post" VALUES (2,'Teste msg Manuel','2020-04-11 16:46:20.399568',2,NULL);
INSERT INTO "post" VALUES (3,'Teste 2 Msg Manuel','2020-04-11 16:46:20.399568',2,NULL);
INSERT INTO "post" VALUES (4,'Teste msg Pedro','2020-04-11 16:46:20.399568',3,NULL);
INSERT INTO "post" VALUES (5,'Teste msg Miguel','2020-04-11 16:46:20.399568',4,NULL);
INSERT INTO "post" VALUES (6,'Teste msg Kelzia','2020-04-11 16:46:20.399568',5,NULL);
INSERT INTO "post" VALUES (7,'Today is a nice day to test python code!','2020-04-11 16:47:48.108672',2,NULL);
INSERT INTO "post" VALUES (8,'I am thinking about this! Could be nice!','2020-04-11 16:49:07.983813',3,NULL);
INSERT INTO "post" VALUES (9,'Testando outras funcionalidades.... :)','2020-04-11 16:50:38.599712',2,NULL);
INSERT INTO "post" VALUES (10,'😊 Agora ficou bonito','2020-04-11 16:51:13.648157',2,NULL);
INSERT INTO "post" VALUES (11,'ola','2020-04-11 17:03:52.859927',2,NULL);
INSERT INTO "post" VALUES (12,'I continue testing code!

I need more lines!','2020-04-11 18:14:21.003150',2,NULL);
INSERT INTO "post" VALUES (13,'Another teste to obtain lines do page down','2020-04-11 18:14:39.410222',2,NULL);
INSERT INTO "post" VALUES (14,'Another teste to obtain lines do page down','2020-04-11 18:14:42.122664',2,NULL);
INSERT INTO "post" VALUES (15,'Another teste to obtain lines do page down','2020-04-11 18:14:44.567875',2,NULL);
INSERT INTO "post" VALUES (16,'Another teste to obtain lines do page down','2020-04-11 18:14:47.527422',2,NULL);
INSERT INTO "post" VALUES (17,'Another teste to obtain lines do page down','2020-04-11 18:14:50.334783',2,NULL);
INSERT INTO "post" VALUES (18,'Say something about this!','2020-04-11 18:15:42.723051',2,NULL);
INSERT INTO "post" VALUES (19,'Test with Bootstrap','2020-04-11 20:31:01.628114',2,NULL);
INSERT INTO "post" VALUES (20,'Good Easter!','2020-04-11 20:52:59.696665',2,NULL);
INSERT INTO "post" VALUES (21,'hello my friend. I arrive just now!','2020-04-11 22:11:59.928977',2,NULL);
INSERT INTO "post" VALUES (22,'I''m going sleep','2020-04-12 02:06:01.532663',2,NULL);
INSERT INTO "post" VALUES (23,'Aqui a pensar nestas traduções,','2020-04-12 20:53:52.145542',2,NULL);
INSERT INTO "post" VALUES (24,'Teste com link do Youtube:

','2020-04-12 20:55:11.669430',2,NULL);
INSERT INTO "post" VALUES (25,'https://www.youtube.com/watch?v=9R2daHWQFB4
','2020-04-12 20:56:09.688836',2,NULL);
INSERT INTO "post" VALUES (26,'Estava aqui a pensar se este tradutor vai funcionar...ou não!   Vamos testar!','2020-04-12 23:56:31.309740',2,'ca');
INSERT INTO "post" VALUES (27,'Quando as coisas não funcionam bem, o mundo vai mal!','2020-04-12 23:58:04.756693',2,'pt');
INSERT INTO "post" VALUES (28,'one and two','2020-04-12 23:58:04.756693',2,'en');
INSERT INTO "post" VALUES (29,'one two tree five','2020-04-12 23:58:04.756693',2,'en');
INSERT INTO "post" VALUES (30,'tree five','2020-04-12 23:58:04.756693',2,'en');
INSERT INTO "post" VALUES (31,'two four ','2020-04-12 23:58:04.756693',2,'en');
INSERT INTO "post" VALUES (32,'one five','2020-04-12 23:58:04.756693',2,'en');
INSERT INTO "post" VALUES (33,'Cansei deste capitulo one, two, four','2020-04-15 20:48:24.299066',2,'ro');
INSERT INTO "post" VALUES (34,'tenho de testar isto urgente!','2020-04-15 20:51:05.065929',2,'pt');
INSERT INTO "post" VALUES (35,'Mais um teste do capitulo','2020-04-15 22:06:48.973176',2,'pt');
INSERT INTO "post" VALUES (36,'capitulo dificil mais um','2020-04-15 22:07:03.364560',2,'pt');
INSERT INTO "user" VALUES (1,'Susan','susan@example.com','pbkdf2:sha256:150000$1ZjhQQwC$8f86d34f2d13d25bbb259be0b88a3a018dc21d8d3dc46fe4917afc6f0d7bc0c2','I''m a beautiful girl that works with SAP in Aço Cearense','2020-04-11 19:51:51.357249');
INSERT INTO "user" VALUES (2,'Manuel','manuel.robalinho@gmail.com','pbkdf2:sha256:150000$DZngZeZ6$c98b0f67295aa5ed263d72d3ecf82f2ff1f17861046bb5d74ce5c908035834ce','I''m a portuguese guy, born in Porto, and i like work with FLASK.
I live in Brazil, in Fortaleza. Now we are at 2020.
','2020-04-15 22:07:16.398093');
INSERT INTO "user" VALUES (3,'Pedro','probalinho@gmail.com','pbkdf2:sha256:150000$L55NMuIk$d84ebe61d51a9347dfc12a40090b3744ab95588c0f3a2943895f48630b32bd94','Test from pedro','2020-04-11 16:49:21.082049');
INSERT INTO "user" VALUES (4,'Miguel','mrobalinho@gmail.com','pbkdf2:sha256:150000$1JnKD8Cc$b8d1485bddbcc4f978337c9a8d7a10ff86882bb6900dc975ee7005cb827d00e2','Test to Miguel Profile','2020-04-11 14:26:28.033379');
INSERT INTO "user" VALUES (5,'Kelzia','kelzia.sousa@gmail.com','pbkdf2:sha256:150000$9kUgVVz2$567d571182f7183adf745e3b8782e8fd4e23d7ed38d62444e67f6530582a4c7c','Test to Kelzia Profile','2020-04-11 14:27:42.921735');
INSERT INTO "user" VALUES (6,'Paulo','paulo@gmail.com','pbkdf2:sha256:150000$CYEKwAjU$2841d640b2a82b2d0fbcd5132b2b9b9885d6282ae2b420e0563ac96bf9419004',NULL,'2020-04-11 20:37:35.483385');
INSERT INTO "alembic_version" VALUES ('ca4ea41e8c1b');
CREATE INDEX IF NOT EXISTS "ix_post_timestamp" ON "post" (
	"timestamp"
);
CREATE UNIQUE INDEX IF NOT EXISTS "ix_user_username" ON "user" (
	"username"
);
CREATE UNIQUE INDEX IF NOT EXISTS "ix_user_email" ON "user" (
	"email"
);
COMMIT;
