/* * PROJECT: Stargate Node v2
 * ACTION: BQL Sector Momentum Audit
 * DATA: Street Momentum (2.4) vs. Stargate DRAM Alpha
 */

/*
-- BQL TERMINAL QUERY:
get(
    weights(universe='SPX Index', group_by=sector) as #current_weight,
    diff(weights(universe='SPX Index', group_by=sector), -30d) as #weight_delta
) 
for(group_by(sector))
*/

CREATE TABLE SG26_SECTOR_MOMENTUM (
    SECTOR_NAME   VARCHAR2(100),
    WEIGHT_DELTA  NUMBER(5,2),
    SYNC_TIME     TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO SG26_SECTOR_MOMENTUM (SECTOR_NAME, WEIGHT_DELTA) VALUES ('Information Tech', 2.4);
INSERT INTO SG26_SECTOR_MOMENTUM (SECTOR_NAME, WEIGHT_DELTA) VALUES ('Energy', -1.8);

COMMIT;
