--extract
SELECT
    gcc.segment1              AS "Segment1",
    gcc.segment2              AS "Segment2",
    gcc.segment3              AS "Segment3",
    gcc.segment4              AS "Segment4",
    gcc.segment5              AS "Segment5",
    gcc.segment6              AS "Segment6",
    gcc.segment7              AS "Segment7",
    gcc.segment8              AS "Segment8",
    gcc.segment9              AS "Segment9",
    gcc.segment10             AS "Segment10",
    gcc.segment11             AS "Segment11",
    gcc.segment12             AS "Segment12",
    gcc.segment13             AS "Segment13",
    gcc.segment14             AS "Segment14",
    gcc.segment15             AS "Segment15",
    gcc.segment16           as "Segment16",
    gcc.segment17             AS "Segment17",
    gcc.SEGMENT18             AS "Segment18",
    gcc.segment19             AS "Segment19",
    gcc.segment20             AS "Segment20",
    gcc.segment21             AS "Segment21",
    gcc.segment22             AS "Segment22",
    gcc.segment23             AS "Segment23",
    gcc.segment24             AS "Segment24",
    gcc.segment25             AS "Segment25",
    gcc.segment26             AS "Segment26",
    gcc.segment27             AS "Segment27",
    gcc.segment28             AS "Segment28",
    gcc.segment29             AS "Segment29",
    gcc.segment30             AS "Segment30",
    gb.begin_balance_dr       AS "Beg Balance DR",
    gb.begin_balance_cr       AS "Beg Balance CR",
    gb.period_net_dr          AS "Period Net DR",
    gb.period_net_cr          AS "Period Net CR",
    ( gb.begin_balance_dr - gb.begin_balance_cr ) + ( gb.period_net_dr - gb.period_net_cr ) AS "YTD Balance",
    ( gb.period_net_dr - gb.period_net_cr ) AS "Periodic Balance",
    CASE
        WHEN account_type IN (
            'A',
            'L',
            'O'
        ) THEN
            ( ( gb.begin_balance_dr - gb.begin_balance_cr ) + ( gb.period_net_dr - gb.period_net_cr ) )
        WHEN account_type IN (
            'R',
            'E'
        ) THEN
            ( gb.period_net_dr - gb.period_net_cr )
        ELSE
            ( gb.period_net_dr - gb.period_net_cr )
    END AS "Balance by Acct Type",
    gb.begin_balance_dr_beq   AS "Func Eq Beg Bal DR",
    gb.begin_balance_cr_beq   AS "Func Eq Beg Bal DR",
    gb.period_net_dr_beq      AS "Func Eq Period Net DR",
    gb.period_net_cr_beq      AS "Func Eq Period Net CR",
    ( gb.begin_balance_dr_beq - gb.begin_balance_cr_beq ) + ( gb.period_net_dr_beq - gb.period_net_cr_beq ) AS "Func Eq YTD Balance "
    ,
    ( gb.period_net_dr_beq - gb.period_net_cr_beq ) AS "Func Eq Periodic Balance",
    CASE
        WHEN account_type IN (
            'A',
            'L',
            'Q'
        ) THEN
            ( ( gb.begin_balance_dr - gb.begin_balance_cr ) + ( gb.period_net_dr - gb.period_net_cr ) )
        WHEN account_type IN (
            'R',
            'E'
        ) THEN
            ( gb.period_net_dr - gb.period_net_cr )
        ELSE
            ( gb.period_net_dr - gb.period_net_cr )
    END AS "Func Eq Balance by Acct Type",
    gld.ledger_id             AS "Ledger ID",
    gld.name                  AS "Ledger Name",
    gb.period_year            AS "Period Year",
    gb.period_name            AS "Period Name",
    gb.period_num             AS "Perion Number",
    gcc.account_type          AS "Acoount Type",
    gb.code_combination_id    AS "Code Combination ID",
    gb.currency_code          AS "Currecy Code",
    gb.actual_flag            AS "Balance Type",
    gb.budget_version_id      AS "Budget Version ID",
    gb.encumbrance_type_id    AS "Encumbrance Type ID",
    gb.translated_flag        AS "Translated",
    gb.period_type            AS "Period Type",
    gcc.enabled_flag          AS "Enabled",
    gcc.summary_flag          AS "Summary Account"
FROM
    gl_balances            gb,
    gl_code_combinations   gcc,
    gl_ledgers             gld
WHERE
    ( 1 = 1 )
    AND gcc.code_combination_id = gb.code_combination_id
    AND gb.actual_flag = 'A'
    AND gb.template_id IS NULL
    AND gld.ledger_id = gb.ledger_id
        AND gld.name = ~LEDGER~  AND gb.PERIOD_NAME = ~ period ~ ;
--Drill
SELECT
    c.concatenated_segments   AS "GL Account",
    a.name                    AS "Journal Name",
    a.je_category             AS "Category",
    a.je_source               AS "Source",
    a.description             AS "Line Description",
    a.currency_code           AS "Currency",
    b.entered_dr              AS "Entered DR",
    b.entered_cr              AS "Entered CR"
FROM
    gl_je_headers              a,
    gl_je_lines                b,
    gl_code_combinations_kfv   c WHERE b.ledger_id = ~LEDGER_ID~ AND B.CODE_COMBINATION_ID = ~CCID~ AND A.PERIOD_NAME = ~PERIOD_NAME~
AND a.je_header_id = b.je_header_id
    AND b.code_combination_id = C.code_combination_id ;
    
-- local
SELECT ENTITYX  AS Entity,ACCOUNTX AS Account,UD3X AS Product,AMOUNTX  
AS Amount , L.PARTname, T.PERIODKEY
FROM  TDATASEG T, TPOVPARTITION L, TPOVPERIOD P 
WHERE  T.PARTITIONKEY = L.PARTITIONKEY  AND  T.PERIODKEY = P.PERIODKEY 

--#agent?QUERY=EBS GL Balance Drill&LEDGER_ID=$ATTR2$&PERIOD_NAME=$ATTR3$&CCID=$ATTR1$&