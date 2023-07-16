UPDATE "{{ table }}"
SET "date"="{{ date }}", "timespan"={{ timespan }}, "is_special"={{ is_special}}, "special_sum"={{ special_sum }}
WHERE "rowid"={{ rowid }}