def parent(i):
    return (i - 1) // 2
def left(i):
    return 2 * i + 1
def right(i):
    return 2 * i + 2
def heapify_up(heap, i):
    while i > 0 and heap[parent(i)][0] < heap[i][0]:
        heap[parent(i)], heap[i] = heap[i], heap[parent(i)]
        i = parent(i)
def heapify_down(heap, i):
    size = len(heap)
    largest = i
    l = left(i)
    r = right(i)
    if l < size and heap[l][0] > heap[largest][0]:
        largest = l
    if r < size and heap[r][0] > heap[largest][0]:
        largest = r
    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        heapify_down(heap, largest)
def insert_job(heap, priority, job_name):
    heap.append((priority, job_name))
    heapify_up(heap, len(heap) - 1)
def extract_max(heap):
    if not heap:
        return None
    if len(heap) == 1:
        return heap.pop()
    max_job = heap[0]
    heap[0] = heap.pop()
    heapify_down(heap, 0)
    return max_job
def peek(heap):
    if heap:
        return heap[0]
    return None
def display(heap):
    print("Jobs in schedule (priority, job):")
    for job in heap:
        print(job)
heap = []
insert_job(heap, 5, "Job A")
insert_job(heap, 3, "Job B")
insert_job(heap, 10, "Job C")
insert_job(heap, 1, "Job D")
print("After inserting jobs:")
display(heap)
print("\nPeek highest priority job:")
print(peek(heap))
print("\nExtract highest priority job:")
max_job = extract_max(heap)
print(max_job)
print("\nJobs after extracting max:")
display(heap)
