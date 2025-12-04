def solution(id_list, report, k):
    report_count = {}
    mail_count = {}
    for i in id_list:
        report_count[i] = 0
        mail_count[i] = 0

    for i in set(report):
        report_count[i.split()[1]] += 1
    
    for i in set(report):
        if report_count[i.split()[1]] >= k:
            mail_count[i.split()[0]] += 1

    return list(mail_count.values())