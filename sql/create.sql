CREATE TABLE films (
    id VARCHAR(255) NOT NULL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    released DATE,
    runtime INT,
    genre VARCHAR(100),
    director VARCHAR(100),
    writer VARCHAR(100),
    actors VARCHAR(500),
    poster_url VARCHAR(500),
    ratings FLOAT,
    language VARCHAR(100),
    plot VARCHAR(2000)
);

