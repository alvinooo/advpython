BEGIN TRANSACTION;
CREATE TABLE BookCatalog(
        id INTEGER NOT NULL PRIMARY KEY,
        author TEXT,
        title TEXT,
        notes CHAR(60),
        copies INTEGER);
INSERT INTO "BookCatalog" VALUES(101,'Hugo, Victor','Les Miserables','Classic',1);
INSERT INTO "BookCatalog" VALUES(102,'Crichton, Michael','Jurassic Park','Science Fiction',3);
INSERT INTO "BookCatalog" VALUES(103,'Grisham, John','The Firm','Fiction',2);
INSERT INTO "BookCatalog" VALUES(104,'Buffett, Jimmy','Tales From Margaritaville','Autobiography',1);
COMMIT;
