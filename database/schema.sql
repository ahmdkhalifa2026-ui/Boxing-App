CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT,
    weight_class VARCHAR(50),
    height DECIMAL(3,2),
    reach DECIMAL(3,2)
);

CREATE TABLE performance_metrics (
    id SERIAL PRIMARY KEY,
    player_id INT REFERENCES players(id),
    strength INT,
    speed INT,
    stamina INT,
    skills INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE training_sessions (
    id SERIAL PRIMARY KEY,
    player_id INT REFERENCES players(id),
    session_date DATE,
    duration INT,
    focus_area VARCHAR(100),
    notes TEXT
);

CREATE TABLE matches (
    id SERIAL PRIMARY KEY,
    player_id INT REFERENCES players(id),
    opponent_id INT REFERENCES players(id),
    match_date DATE,
    round_count INT,
    result VARCHAR(50)  -- Win, Loss, Draw
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE reports (
    id SERIAL PRIMARY KEY,
    player_id INT REFERENCES players(id),
    report_date DATE,
    content TEXT
);
