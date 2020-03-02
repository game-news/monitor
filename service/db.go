package service

import (
	"database/sql"
	"fmt"
	"log"

	_ "github.com/lib/pq"
)

func ConnectDB() {
	connStr := "postgres://niracler:123456@localhost/gamenews_db?sslmode=disable"
	db, err := sql.Open("postgres", connStr)
	if err != nil {
		log.Fatal(err)
	}

	rows, err := db.Query(`SELECT * FROM users_userprofile`)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(rows)
}
