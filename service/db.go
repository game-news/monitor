package service

import (
	"fmt"
	"log"

	"gamenews.niracler.com/monitor/model"
	"gamenews.niracler.com/monitor/setting"
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/postgres"
)

var db *gorm.DB

func ConnectDB() {
	var (
		err                                               error
		dbType, dbName, user, password, host, tablePrefix string
	)

	sec, err := setting.Cfg.GetSection("database")
	if err != nil {
		log.Fatal(2, "Fail to get section 'database': %v", err)
	}

	dbType = sec.Key("TYPE").String()
	dbName = sec.Key("NAME").String()
	user = sec.Key("USER").String()
	password = sec.Key("PASSWORD").String()
	host = sec.Key("HOST").String()
	tablePrefix = sec.Key("TABLE_PREFIX").String()

	db, err = gorm.Open(dbType, fmt.Sprintf("host=%s user=%s dbname=%s sslmode=disable password=%s",
		host,
		user,
		dbName,
		password,
	))

	if err != nil {
		log.Println(err)
	}

	gorm.DefaultTableNameHandler = func(db *gorm.DB, defaultTableName string) string {
		return tablePrefix + defaultTableName
	}

	// db表迁移:
	db.SingularTable(true)
	if err = db.AutoMigrate(&model.Game{}).Error; nil != err {
		log.Fatal("auto migrate tables failed: " + err.Error())
	}

	db.DB().SetMaxIdleConns(10)
	db.DB().SetMaxOpenConns(100)
	// db.LogMode(model.Conf.ShowSQL)
}

func GetDB() *gorm.DB {
	return db
}

func CloseDB() {
	defer db.Close()
}
