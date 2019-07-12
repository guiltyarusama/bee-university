from __future__ import print_function
import concurrent.futures
import requests
import time
import sys


def multithread_helper(items, method, max_workers=5, timeout_concurrent_by_second=180, debug=True):
    output = []
    start = time.time()
    print('start:', start)
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_item = {executor.submit(method, item): item for item in items}
        # print('future_to_item', future_to_item)
        print('loading multithread ' + str(method))
        for future in concurrent.futures.as_completed(future_to_item, timeout=timeout_concurrent_by_second):
            item = future_to_item[future]
            try:
                data = future.result()
                if data is not None and data != '':
                    output.append(data)
                # print(data)
            except Exception as e:
                # print('%r generated an exception: %s' % (item, exc))
                print(future)
                print(e)
                print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            else:
                if debug:
                    print('"%s" fetched in %ss' % (item, (time.time() - start)))
    if debug:
        print("Elapsed Time: %ss" % (time.time() - start))
    return output


def multithread_helper_append_array(items, method, max_workers=5, timeout_concurrent_by_second=180, debug=True):
    output = []
    start = time.time()
    print('start:', start)
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_item = {executor.submit(method, item): item for item in items}
        # print('future_to_item', future_to_item)
        print('loading multithread ' + str(method))
        for future in concurrent.futures.as_completed(future_to_item, timeout=timeout_concurrent_by_second):
            item = future_to_item[future]
            try:
                data = future.result()
                if data is not None and len(data) > 0:
                    output += data
                # print(data)
            except Exception as e:
                # print('%r generated an exception: %s' % (item, exc))
                print(future)
                print(e)
                print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            else:
                if debug:
                    print('"%s" fetched in %ss' % (item, (time.time() - start)))
    if debug:
        print("Elapsed Time: %ss" % (time.time() - start))
    return output


def multithread_helper_without_array(items, method, max_workers=5, timeout_concurrent_by_second=180, debug=True):
    output = ''
    start = time.time()
    # print('start:', start)
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_item = {executor.submit(method, item): item for item in items}
        # print('future_to_item', future_to_item)
        print('loading multithread ' + str(method))
        pos = 0
        for future in concurrent.futures.as_completed(future_to_item, timeout=timeout_concurrent_by_second):
            item = future_to_item[future]
            try:
                data = future.result()
                if data is not None:
                    if pos == 0:
                        output = data
                    else:
                        output += '\n' + data
                    # print(data)
                    pos += 1
            except Exception as e:
                # print('%r generated an exception: %s' % (item, exc))
                print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            else:
                if debug:
                    print('"%s" fetched in %ss' % (item, (time.time() - start)))
    if debug:
        print("Elapsed Time: %ss" % (time.time() - start))
    return output


# Retrieve a single page and report the url and contents
def method_mock(url):
    conn = requests.get(url)
    # conn = requests.get(url, timeout=options['timeout'])
    # print(conn.text)
    return conn.text


def main():
    urls = ["http://www.google.com", "http://www.apple.com", "http://www.microsoft.com", "http://www.amazon.com",
            "http://www.facebook.com"]
    multithread_helper(items=urls, method=method_mock, max_workers=5)

# main()
