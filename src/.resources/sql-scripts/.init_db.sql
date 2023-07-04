CREATE TABLE IF NOT EXISTS "STUDENTS" (
	"name"	TEXT UNIQUE,
	"hour_cost"	REAL,
	"currency"	TEXT,
	"table"	TEXT UNIQUE
)