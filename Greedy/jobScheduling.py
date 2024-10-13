import heapq

class Job:
    # Job class which stores profit, deadline, and id.
    
    def __init__(self, job_id, profit, deadline):
        self.id = job_id
        self.profit = profit
        self.deadline = deadline

class Solution:
    
    # Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self, Jobs, n):
        
        # Sorting jobs according to descending order of profit
        Jobs.sort(key=lambda x: x.profit, reverse=True)
        
        # Finding the maximum deadline
        max_deadline = max(job.deadline for job in Jobs)
        
        # Initializing slots and results
        slots = [-1] * (max_deadline + 1)
        totalProfit = 0
        jobCount = 0
        
        # Iterating through each job to find a slot
        for job in Jobs:
            # Finding a slot for this job
            for j in range(job.deadline, 0, -1):
                if slots[j] == -1:
                    slots[j] = job.id
                    totalProfit += job.profit
                    jobCount += 1
                    break
        
        return (jobCount, totalProfit)

# Example usage
jobs = [Job(1, 100, 2), Job(2, 19, 1), Job(3, 27, 2), Job(4, 25, 1), Job(5, 15, 3)]
n = len(jobs)
solution = Solution()
print(solution.JobScheduling(jobs, n))  # Output: (Number of jobs done, Total profit)