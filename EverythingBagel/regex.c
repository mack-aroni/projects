#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>

// define node types for the tree
typedef enum
{
  GROUP,
  CHARACTER,
  STAR,
  QUESTION_MARK,
  DOT
} NodeType;

// define tree node structure
typedef struct Node
{
  NodeType type;
  char value;
  struct Node *left;
  struct Node *right;
} Node;

// helper function to create a new node
Node *createNode(NodeType type, char value)
{
  Node *newNode = (Node *)malloc(sizeof(Node));
  if (newNode == NULL)
  {
    fprintf(stderr, "Memory allocation failed\n");
    exit(EXIT_FAILURE);
  }
  newNode->type = type;
  newNode->value = value;
  newNode->left = NULL;
  newNode->right = NULL;
  return newNode;
}

// Function to print binary tree in 2D
// It does reverse inorder traversal
void print2DUtil(struct Node *root, int space)
{
  int COUNT = 5;
  // Base case
  if (root == NULL)
    return;

  // Increase distance between levels
  space += COUNT;

  // Process right child first
  print2DUtil(root->right, space);

  // Print current node after space
  // count
  printf("\n");
  for (int i = COUNT; i < space; i++)
    printf(" ");
  printf("%c\n", root->value);

  // Process left child
  print2DUtil(root->left, space);
}

// Wrapper over print2DUtil()
void print2D(struct Node *root)
{
  // Pass initial space count as 0
  print2DUtil(root, 0);
}

// function to parse regular expression and construct the tree
Node *parseRegex(char *regex)
{
  Node *root = NULL;
  Node *current = NULL;
  Node *holding = NULL;

  int i = 0;
  // iterate over regex to create a parse tree
  // for (int i = 0; regex[i] != '\0'; i++)
  while (regex[i] != '\0')
  {
    char c = regex[i];
    // printf("char: %c\n", c);

    if (c == '*' || c == '?')
    {
      Node *newNode;
      if (c == '*')
        newNode = createNode(STAR, '*');
      else
        newNode = createNode(QUESTION_MARK, '?');

      // after a char or dot
      if (holding != NULL)
      {
        // second node
        if (root == NULL)
        {
          root = newNode;
          root->left = holding;
          current = newNode;
        }
        // regular case
        else
        {
          current->right = newNode;
          current = newNode;
          current->left = holding;
        }
        holding = NULL;
      }
      // after another symbol
      else
      {
        current->right = newNode;
        current = newNode;
      }
      i++;
    }
    // char, group, or dot case
    else
    {
      Node *newNode;
      if (c == '.')
        newNode = createNode(DOT, '.');
      if (c == '(')
      {
        // track begining and end of ()
        int j = i + 1;
        while (regex[j] != '\0')
        {
          if (regex[j] == ')')
            break;
          j++;
        }

        // turn inside of group into subexpr
        char *subexpr = (char *)malloc((j - i) * sizeof(char));
        strncpy(subexpr, regex + i + 1, j - i - 1);
        subexpr[j - i - 1] = '\0';

        newNode = createNode(GROUP, 'g');
        // parse subexpr into left of group node
        newNode->left = parseRegex(subexpr);
        // move to the character after the closing parentheses
        i = j;
      }
      else
        newNode = createNode(CHARACTER, c);

      // after a char or a dot
      if (holding != NULL)
      {
        // second node
        if (root == NULL)
        {
          root = holding;
          current = root;
          holding = newNode;
        }
        // regular case
        else
        {
          current->right = holding;
          current = holding;
          holding = newNode;
        }
      }
      // regular case
      else
      {
        holding = newNode;
      }
      i++;
    }

    // test prints
    // if (root != NULL)
    //   printf("root: %c ", root->value);
    // if (current != NULL)
    //   printf("current: %c ", current->value);
    // if (holding != NULL)
    // {
    //   printf("holding: %c ", holding->value);
    //   if (holding->left != NULL)
    //     printf("hleft: %c ", holding->left->value);
    // }
    // printf("\n");
  }

  if (holding != NULL)
  {
    if (root == NULL)
      root = holding;
    else
      current->right = holding;
  }

  return root;
}

// helper function to parse a group subtree of a regex tree
// returns i if group is contained in substr of str, else returns 0
int parseSubTree(Node *node, char *str)
{
  int i = 0;
  while (*str + i != '\0' && (*str + i == node->value || node->type == DOT))
  {
    // printf("%c\n", *str + i);
    // printf("%c\n", node->value);
    if (node->right != NULL)
    {
      node = node->right;
      i++;
    }
    else
    {
      return i + 1;
    }
  }
  return 0;
}

// recursive function to match string against the regex tree
bool parseTree(Node *root, char *str)
{
  // base case
  if (root == NULL)
  {
    return *str == '\0';
    // return true;
  }

  // printf("value: %c char: %c\n", root->value, *str);

  // switch case off of current tree node type
  switch (root->type)
  {
  case DOT:
    return (*str != '\0' && *str != '\n') && parseTree(root->right, str + 1);

  case GROUP:
    // iterate over group subtree once
    int x = parseSubTree(root->left, str);
    if (x == 0)
    {
      return false;
    }
    str += x;
    return parseTree(root->right, str);

  case STAR:
    // group case
    if (root->left->type == GROUP)
    {
      // iterate str over group subtree until no longer matches
      while (parseSubTree(root->left->left, str) != 0)
      {
        str += parseSubTree(root->left->left, str);
      }
      return parseTree(root->right, str);
    }
    // char case
    else
    {
      while (*str != '\0' && (*str == root->left->value || root->left->type == DOT))
      {
        if (parseTree(root->right, str))
        {
          return true;
        }
        str++;
      }
      return parseTree(root->right, str);
    }

  case QUESTION_MARK:
    // group case
    if (root->left->type == GROUP)
    {
      // iterate over group subtree once
      str += parseSubTree(root->left->left, str);
      return parseTree(root->right, str);
    }
    // char case
    else if (*str != '\0' && (*str == root->left->value || root->left->type == DOT))
    {
      if (parseTree(root->right, str))
      {
        return true;
      }
      str++;
    }
    return parseTree(root->right, str);

  case CHARACTER:
    return (*str == root->value) && parseTree(root->right, str + 1);

  default:
    fprintf(stderr, "Unknown node type\n");
    exit(EXIT_FAILURE);
  }
}

// helper func that checks if the regex phrase is valid
bool validRegex(char *regex)
{
  bool paren = false;
  int count = 0;
  for (int i = 0; regex[i] != '\0'; i++)
  {
    // parentheses tracking and nested parentheses checking
    if (regex[i] == '(')
    {
      count = 0;
      // ((... situation
      if (paren)
      {
        fprintf(stderr, "Invalid regular expression\n");
        return false;
      }
      // new (...
      else
      {
        paren = true;
      }
    }
    else if (regex[i] == ')')
    {
      // complete parentheses (...)
      if (paren && count > 1)
      {
        paren = false;
      }
      // )... or () situation
      else
      {
        fprintf(stderr, "Invalid regular expression\n");
        return false;
      }
    }
    // expression starts as *. or ?. or ).
    if (i == 0 && (regex[i] == '*' || regex[i] == '?' || regex[i] == ')'))
    {
      fprintf(stderr, "Invalid regular expression\n");
      return false;
    }
    // expression contains sequential symbols **, *?, ?*, ?? or symbols inside parentheses
    else if ((regex[i] == '*' || regex[i] == '?') && !paren && (regex[i - 1] == '*' || regex[i - 1] == '?'))
    {
      fprintf(stderr, "Invalid regular expression\n");
      return false;
      // }
    }
    count++;
  }
  return true;
}

// main call function for regex matching
bool match(char *regex, char *str)
{
  // printf("inputs: %s %s\n", regex, str);
  // printf("valid: %s\n", validRegex(regex) ? "true" : "false");

  // check regex phrase, create regex tree, compare with str
  if (validRegex(regex))
  {
    Node *regexTree;
    regexTree = parseRegex(regex);
    print2D(regexTree);
    int i = 0;
    bool res = false;

    // check all indices of the str for regex matches
    while (str[i] != '\0')
    {
      printf("STRING: %s\n", str + i);
      res = parseTree(regexTree, str + i);
      printf("RES: %s\n", res ? "true" : "false");
      if (res)
      {
        break;
        i++;
      }
    }

    free(regexTree);
    return res;
  }
  return false;
  // exit(EXIT_FAILURE);
}

int main(int argc, char *argv[])
{
  char regex[strlen(argv[1]) + 1];
  strcpy(regex, argv[1]);

  if (match(regex, argv[2]))
    printf("MATCH\n");
  else
    printf("NO MATCH\n");

  return 0;
}