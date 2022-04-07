/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
const levelOrderBottom = (root)=> {
    if(!root) return []
    
    const queue = [root]
    const results = []
    
    while(queue.length){
        let len = queue.length
        results.push(queue.map(one => one.val))
        
        while(len--){
           let node =  queue.shift()
           if(node.left) queue.push(node.left)
            if(node.right) queue.push(node.right)
        }
    }
    
    return results.reverse()
    
};