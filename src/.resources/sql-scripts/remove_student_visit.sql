DELETE FROM "{{ table }}" WHERE
"date"="{{ date }}" and "timespan"={{ timespan }} and
"is_special"={{ is_special }} and "special_sum"={{ special_sum }}