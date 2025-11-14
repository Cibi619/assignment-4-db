ALTER TABLE subscribers
    ADD COLUMN status VARCHAR(20) NOT NULL DEFAULT 'active';
CREATE INDEX idx_created_at ON subscribers(created_at);
