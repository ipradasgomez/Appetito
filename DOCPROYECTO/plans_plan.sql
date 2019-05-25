BEGIN TRANSACTION;
INSERT INTO "plans_plan" VALUES (1,'GRATIS',1,1,5,3,0,0,'free',0,'¡El más elegido!'),
 (2,'BÁSICO',1,5,5,7,0,15.99,'blue',0,NULL),
 (3,'PRO',0,0,0,0,1,44.99,'standard',1,'¡El más apetitoso :)!');
COMMIT;
